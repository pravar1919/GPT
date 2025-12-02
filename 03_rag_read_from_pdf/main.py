from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

# Load Document
doc = TextLoader("jd.txt")
documents = doc.load()

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)
documents = text_splitter.split_documents(documents)

# 🔥 OpenAI: Embeddings
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
db = FAISS.from_documents(documents, embedding_model)

# 🔥 OpenAI: LLM Provider
llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

# Prompt template
prompt = ChatPromptTemplate.from_template(
    """
    Answer the following question based on the provided context.
    Provide a short, crisp, and accurate response.
    
    <context>
    {context}
    </context>
    
    Question: {input}
    """
)

# Create document chain
doc_chain = create_stuff_documents_chain(llm, prompt)

# Retriever | k = number of relevant chunks to retrieve
retriever = db.as_retriever(search_kwargs={"k": 4})

# Create RAG retrieval chain
retrieval_chain = create_retrieval_chain(retriever, doc_chain)

# Query
response = retrieval_chain.invoke({"input": "What is the summary of this JD?"})

# Print answer
print("\n📌 Summary:\n", response["answer"])
