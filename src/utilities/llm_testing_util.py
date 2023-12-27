import os
import requests
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint

token = os.environ.get("HF_TOKEN")
API_URL = "https://z8dvl7fzhxxcybd8.eu-west-1.aws.endpoints.huggingface.cloud"
headers = {"Authorization": "Bearer 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"}
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
        endpoint_url="https://z8dvl7fzhxxcybd8.eu-west-1.aws.endpoints.huggingface.cloud",
        task="text2text-generation",
        model_kwargs={
            "max_new_tokens": 200
        }
    )
    return llm.generate(["Hello, how are you?"])
