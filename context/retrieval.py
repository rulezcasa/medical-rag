#imports
import faiss
import numpy as np
from utils.config import model


def retrieve(query, index, chunks, k=3,):
    """
    Retrieves the top-k most relevant text chunks from a FAISS index based on the input query.

    Args:
        query (str): The input query string for which relevant context is to be retrieved.
        index (faiss.Index): A FAISS index containing the precomputed embeddings of the text chunks.
        chunks (List[str]): The original text chunks corresponding to the embeddings in the FAISS index.
        k (int, optional): The number of top similar chunks to retrieve. Defaults to 3.

    Returns:
        List[str]: A list of the top-k most relevant text chunks based on similarity to the query.
    """
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k)
    return [chunks[i] for i in I[0]]
