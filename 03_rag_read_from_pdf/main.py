from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM, OllamaEmbeddings

from langchain.chains import create_retrieval_chain


doc = TextLoader("jd.txt")
documents =  doc.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
documents = text_splitter.split_documents(documents)

db = FAISS.from_documents(documents, OllamaEmbeddings(model="llama3.2"))

llm = OllamaLLM(model="llama3.2")

# design Chatprompt template
from langchain_core.prompts import ChatPromptTemplate
# context is all the documents there are in the vector Database.
# input is the question I am asking.
prompt = ChatPromptTemplate.from_template(
    """
    Answer the following question based on the provided context.
    Think step by step before providing answer.
    Also this is a Job description of a particular company, so answer accordingly.
    <context>
    {context}
    </context>
    Question: {input}
    """
)

# create stuff document chain

doc_chain = create_stuff_documents_chain(llm, prompt)

retriver = db.as_retriever()
retriver

retrival_chain = create_retrieval_chain(retriver, doc_chain)

response = retrival_chain.invoke({"input": "what is the summary of this JD?"})

print(response["answer"])
