#imports
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

def generate(top_chunks, query):
    """
    Generates a natural language answer to a given query using retrieved context and a language model.

    Args:
        top_chunks (List[str]): A list of the most relevant text chunks retrieved from the knowledge base.
        query (str): The input user query for which an answer needs to be generated.

    Returns:
        str: The generated response from the language model, excluding the system prompt.
    """
    
    #model_id="sshleifer/tiny-gpt2"
    model_id = "mistralai/Mistral-7B-Instruct-v0.3"
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    model = AutoModelForCausalLM.from_pretrained(
        model_id, 
        torch_dtype=torch.float16, 
        device_map="cpu" 
    )
    llm = pipeline("text-generation", model=model, tokenizer=tokenizer)

    context = "\n\n".join(top_chunks)
    prompt = f"<s>[INST] <<SYS>>\nYou are a helpful medical assistant.\n<</SYS>>\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer: [/INST]"
    response = llm(prompt, max_new_tokens=300, do_sample=True, temperature=0.7)
    full_output = response[0]["generated_text"]
    answer = full_output.split("[/INST]")[-1].strip()

    return answer


#Context based prompt explained :
"""
  - Top retrieved chunks and joined with core prompt separated by double newlines for clarity.
    - Construct the full prompt using the LLaMA-style format: <s>[INST] ... [/INST]
        - System : "You are a helpful medical assistant"
        - User : Include the context followed by the user’s question
    - Pass the formatted prompt to the LLM for generation with sampling parameters
    - Strip and return the final answer for downstream use or display
"""



