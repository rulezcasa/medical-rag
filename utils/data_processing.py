from PyPDF2 import PdfReader

def load_pdf(file_path):
    """
    Loads and extracts text from all pages of a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The concatenated text extracted from all pages of the PDF, 
             with each page's content separated by a newline character.
    """
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def chunk_text(text, chunk_size=500, overlap=50):
    """
    Splits a large text into overlapping chunks for processing.

    Args:
        text (str): The input text to be split into chunks.
        chunk_size (int, optional): The maximum number of characters in each chunk. Defaults to 500.
        overlap (int, optional): The number of overlapping characters between consecutive chunks. Defaults to 50.

    Returns:
        List[str]: A list of overlapping text chunks.
    """  
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks


#chunking strategy explained :
"""
    - Initilalize an empty list to hold the chunks
    - iterate over the text till end: (Sliding window approach)
        - capture the text from start to chunk_size(arugment)
        - append the chunk to list
        - initialize the start as end-overlap i.e no. of character that needs to be recaptured
    - Finally return chunks for the downstream task
"""

