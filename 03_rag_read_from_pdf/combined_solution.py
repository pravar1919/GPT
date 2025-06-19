from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

from langchain.chains import create_retrieval_chain


# JD
jd_loader = TextLoader("jd.txt")
jd_docs = jd_loader.load()

# Resume
resume_loader = PyPDFLoader("Pravar_Sharma_Resume.pdf")
resume_docs = resume_loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
jd_chunks = splitter.split_documents(jd_docs)
resume_chunks = splitter.split_documents(resume_docs)

combined_docs = jd_chunks + resume_chunks

db = FAISS.from_documents(combined_docs, OllamaEmbeddings(model="llama3.2"))

llm = OllamaLLM(model="llama3.2")

match_prompt = ChatPromptTemplate.from_template(
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

# doc_chain = create_stuff_documents_chain(llm, match_prompt)

# retriver = db.as_retriever()
# retriver

# retrival_chain = create_retrieval_chain(retriver, doc_chain)

chain = LLMChain(llm=llm, prompt=match_prompt)

# Combine all text from JD and Resume
jd_text = "\n\n".join([doc.page_content for doc in jd_chunks])
resume_text = "\n\n".join([doc.page_content for doc in resume_chunks])

response = chain.invoke({"jd": jd_text, "resume": resume_text})
print(response["text"])


from langchain_community.embeddings import OllamaEmbeddings
import numpy as np

embeddings = OllamaEmbeddings(model="llama3.2")

jd_embedding = embeddings.embed_documents([jd_text])
resume_embedding = embeddings.embed_documents([resume_text])

# Average embeddings
jd_avg = np.mean(jd_embedding, axis=0)
resume_avg = np.mean(resume_embedding, axis=0)

# Cosine similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

similarity_score = cosine_similarity(jd_avg, resume_avg)
percentage_match = round(similarity_score * 100, 2)
print(f"Similarity Score: {percentage_match}%")
