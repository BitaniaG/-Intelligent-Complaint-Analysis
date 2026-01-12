class ComplaintRAGPipeline:
    """
    End-to-end RAG pipeline connecting retriever and generator.
    """

    def __init__(self, retriever, generator):
        self.retriever = retriever
        self.generator = generator

    def answer(self, question, top_k=5):
        retrieved_chunks = self.retriever.retrieve(question, top_k)
        answer = self.generator.generate(question, retrieved_chunks)
        return answer, retrieved_chunks
