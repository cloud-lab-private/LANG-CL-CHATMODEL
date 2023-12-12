import unittest
from typing import List

from langchain.chat_models import AzureChatOpenAI
from langchain_core.messages import AIMessage, BaseMessage

from src.main.lab import send_single_human_message, send_human_message_prompt_template, send_multi_message_prompt_template, \
    send_prompt_with_chat_memory


class TestLLMResponses(unittest.TestCase):
    def test_llm_connection(self):
        llm = AzureChatOpenAI(model_name="gpt-35-turbo")
        self.assertIsInstance(llm, AzureChatOpenAI)

    def test_send_single_human_message(self):
        response = send_single_human_message("Hello, how are you?")
        self.assertIsInstance(response, BaseMessage)

    def test_send_human_message_prompt_template(self):
        response = send_human_message_prompt_template("goofy", "Hello, how are you?")
        self.assertIsInstance(response, BaseMessage)

    def test_send_multi_message_prompt_template(self):
        response = send_multi_message_prompt_template("JSON", "How much wood could a woodchuck chuck if a woodchuck could chuck wood?")
        self.assertIsInstance(response, AIMessage)

    def test_send_prompt_with_chat_memory(self):
        response = send_prompt_with_chat_memory("pirate", "How much wood could a woodchuck chuck if a woodchuck could chuck wood?")
        self.assertIsInstance(response, List)
        self.assertIn("woodchuck", response[1].content.lower())


if __name__ == '__main__':
    unittest.main()
