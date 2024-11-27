import os
import openai

openai_api_key = os.getenv("OPENAI_API_KEY")
# openai_api_key = "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"
# openai_api_key = "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"
openai.api_key = openai_api_key


def ask_chatbot(question: str, context: str = "You are a helpful assistant.") -> str:
    if not openai.api_key:
        raise ValueError("OpenAI API key not found. Set the OPENAI_API_KEY environment variable.")

    # Use the correct method to interact with the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": question},
        ]
    )
    return response['choices'][0]['message']['content']