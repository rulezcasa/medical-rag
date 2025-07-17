from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from utils.config import model


def generate_and_load(chunks):
    """
    Generates embeddings for a list of text chunks, builds a FAISS index, and saves it to disk.

    Args:
        chunks (List[str]): A list of text segments to embed and index.

    Returns:
        None
    """
    embeddings = model.encode(chunks)
    dimension = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    faiss.write_index(index, "data/faiss_index.index")