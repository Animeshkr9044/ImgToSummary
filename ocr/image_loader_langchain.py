from langchain_community.document_loaders.image import UnstructuredImageLoader
import warnings

warnings.filterwarnings("ignore")


def get_image_langchain_content(image_path):
    """
    Extracts text from an image using the UnstructuredImageLoader class from the langchain_community library.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The text extracted from the image.
    """
    loader = UnstructuredImageLoader(image_path)
    data = loader.load()
    image_content = data[0].page_content
    return image_content

# here are more thing to come now
