from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

Open_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=Open_api_key)


def summarize_text_using_openai(text, model="gpt-4o"):
    """
    Summarizes text using OpenAI's GPT model.

    Args:
        text (str): The text to be summarized.
        model (str, optional): The GPT model to use. Defaults to "gpt-3.5-turbo".

    Returns:
        str: The summarized text.
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user",
             "content": f"Summarize this text in not more than 100 words trying to capture each real detail: {text}"}
        ],
        temperature=0.0,
    )

    output = response.choices[0].message.content.lstrip('```json').rstrip('```')

    return output
