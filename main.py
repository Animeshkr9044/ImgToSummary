from ocr.image_loader_langchain import get_image_langchain_content
from preprocessing.text_preprocessing import preprocess_text
from llm.openai_model import summarize_text_using_openai
import os

def main():
    # Get the image path from the command line argument
    image_path = os.path.abspath(os.sys.argv[1])

    # Extract text from the image
    image_text = get_image_langchain_content(image_path)

    # Preprocess the text
    preprocessed_text = preprocess_text(image_text)

    # Summarize the text using OpenAI's GPT model
    summarized_text = summarize_text_using_openai(preprocessed_text)

    # Print the summarized text
    print(summarized_text)

if __name__ == "__main__":
    main()
