from transformers import pipeline


class ComplaintGenerator:
    """
    Generates grounded answers based on retrieved complaint context.
    """

    def __init__(self, model_name="google/flan-t5-base"):
        self.generator = pipeline(
            "text2text-generation",
            model=model_name,
            max_length=300
        )

    def build_prompt(self, question: str, contexts: list) -> str:
        """
        Builds a grounded prompt for the language model.
        """
        context_text = "\n\n".join(
            [f"- {c['text']}" for c in contexts]
        )

        prompt = f"""
You are an analyst at a financial institution.

Use ONLY the following customer complaints to answer the question.
Do not add information not supported by the complaints.

Customer Complaints:
{context_text}

Question:
{question}

Answer:
"""
        return prompt.strip()

    def generate(self, question: str, contexts: list) -> str:
        prompt = self.build_prompt(question, contexts)
        response = self.generator(prompt)[0]["generated_text"]
        return response
