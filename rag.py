from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

class RAGDocument():

    def loadDocument(self, file_path: str):
        loader = PyPDFLoader(file_path)
        self.documents = loader.load()
        print(f"Loaded {len(self.documents)} documents from {file_path}")
        print(f"{self.documents[0].page_content[:200]}\n")
        print(self.documents[0].metadata)

    def splitDocument(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            add_start_index=True
        )
        self.split_documents = text_splitter.split_documents(self.documents)
        print(f"Split into {len(self.split_documents)} chunks")

    def embedDocuments(self):
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
        self.embedded_documents = self.embeddings.embed_documents(
            [doc.page_content for doc in self.split_documents]
        )
        print(f"Embedded {len(self.embedded_documents)} chunks")
        vector_1 = self.embeddings.embed_query(self.split_documents[0].page_content)
        print(vector_1[:10])
        
    def storeVectorDocuments(self):
        self.vector_store = InMemoryVectorStore.from_documents(
            self.split_documents,  # Pass the split Document objects, not embeddings
            self.embeddings             # Pass the embedding model
        )

    def getDocumentForQuery(self, query: str):
        results = self.vector_store.similarity_search(query)
        print(f"Found {len(results)} relevant documents for the query.")
        return results[0]

    def getDocumentWithRetrievers(self, messages: list):
        retriever = self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 1},
        )

        result = retriever.batch(messages)
        return result;
        
    

    

