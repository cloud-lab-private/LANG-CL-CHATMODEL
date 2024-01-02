import os
import requests
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint

token = os.environ['HF_TOKEN']
API_URL = os.environ['LLM_ENDPOINT']
headers = {"Authorization": f"Bearer {token}"}
textInput = """
<|system|>
You are a pirate chatbot who always responds with Arr!</s>
<|user|>
{userInput}</s>
<|assistant|>
"""


def llm_wakeup():
    response = requests.post(API_URL, json={
        "inputs": textInput.format(userInput="Hello, how are you?")
    }, headers=headers)
    print(response.json())
    print("################################################")
    print("LLM is waking up...Please try again in 5 minutes.")
    print("################################################")


def llm_connection_check():
    llm = HuggingFaceEndpoint(
        endpoint_url=API_URL,
        task="text2text-generation",
        model_kwargs={
            "max_new_tokens": 200
        }
    )
    return llm.generate(["Hello, how are you?"])
