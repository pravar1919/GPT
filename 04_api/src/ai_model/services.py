from langchain_community.document_loaders import TextLoader, PyPDFLoader, PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import numpy as np
import os

from langchain.chains import create_retrieval_chain


class SimilarityMatch:
    EMBEDDING = OllamaEmbeddings(model="llama3.2")

    def __init__(self, path_to_jd, path_to_resume):
        self.path_to_jd = path_to_jd
        self.path_to_resume = path_to_resume

    def load_resume(self):
        jd_loader = TextLoader(self.path_to_resume, encoding="utf-8", autodetect_encoding=True)
        self.jd_docs = jd_loader.load()

    def load_jd(self):
        resume_loader = PyMuPDFLoader(self.path_to_jd)
        self.resume_docs = resume_loader.load()

    def splitter(self):
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        self.jd_chunks = splitter.split_documents(self.jd_docs)
        self.resume_chunks = splitter.split_documents(self.resume_docs)
        self.combined_docs = self.jd_chunks + self.resume_chunks

    def embedding(self):
        self.db = FAISS.from_documents(self.combined_docs, self.EMBEDDING)
        self.llm = OllamaLLM(model="llama3.2")


    def prompt(self):
        self.match_prompt = ChatPromptTemplate.from_template(
            """
            Given the following Job Description and Resume, compare them and provide:
            1. A matching percentage score (0–100%) indicating how well the candidate matches the job.
            2. A brief justification of the score.
            
            <job_description>
            {jd}
            </job_description>

            <resume>
            {resume}
            </resume>
            """
        )

    def cosine_similarity(self, jd_avg, resume_avg):
        return np.dot(jd_avg, resume_avg) / (np.linalg.norm(jd_avg) * np.linalg.norm(resume_avg))

    def invoke(self):
        self.load_resume()
        self.load_jd()
        self.splitter()
        self.embedding()
        self.prompt()

        chain = self.match_prompt | self.llm

        # Combine all text from JD and Resume
        jd_text = "\n\n".join([doc.page_content for doc in self.jd_chunks])
        resume_text = "\n\n".join([doc.page_content for doc in self.resume_chunks])

        jd_embedding = self.EMBEDDING.embed_documents([jd_text])
        resume_embedding = self.EMBEDDING.embed_documents([resume_text])

        # Average embeddings
        jd_avg = np.mean(jd_embedding, axis=0)
        resume_avg = np.mean(resume_embedding, axis=0)

        description = chain.invoke({"jd": jd_text, "resume": resume_text})
        similarity_score = self.cosine_similarity(jd_avg, resume_avg)
        percentage_match = round(similarity_score * 100, 2)
        return {
            "description": description,
            "score": percentage_match
        }


if __name__ == "__main__":
    s = SimilarityMatch("/Users/pravarsharma/Developer/dev/GPT/03_rag_read_from_pdf/Pravar_Sharma_Resume.pdf", "/Users/pravarsharma/Developer/dev/GPT/03_rag_read_from_pdf/jd.txt")
    print(s.invoke())
