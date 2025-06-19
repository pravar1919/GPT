from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain



loader = PyPDFLoader("pravar_sharma_updated.pdf")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
documents = text_splitter.split_documents(docs)


db = FAISS.from_documents(documents, OllamaEmbeddings(model="llama3.2"))

# query = "RESTful APIs for booking, cancellation"
# result = db.similarity_search(query)
# result[0].page_content



llm = OllamaLLM(model="llama3.2")

prompt = ChatPromptTemplate.from_template(
    """
    Answer the following question based only on the provided context.
    Think step by step before providing answer.
    <context>
    {context}
    </context>
    Question: {input}
    """
)


doc_chain = create_stuff_documents_chain(llm, prompt)

retriver = db.as_retriever()



retrival_chain = create_retrieval_chain(retriver, doc_chain)


response = retrival_chain.invoke(
    {"input": "What are the companies he has worked in so far?"}
)


response["answer"]

response = retrival_chain.invoke({"input": "what is his education?"})


response["answer"]


response = retrival_chain.invoke({"input": ""})
