import os
import unittest
from typing import List

from langchain.chat_models import AzureChatOpenAI
from langchain_community.chat_models import ChatHuggingFace
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage

from src.main.lab import send_single_human_message, send_human_message_prompt_template, send_multi_message_prompt_template, \
    send_prompt_with_chat_memory
from src.utilities.llm_testing_util import llm_connection_check, llm_wakeup


class TestLLMResponses(unittest.TestCase):
    def test_llm_connection(self):
        try:
            response = llm_connection_check()
            print(response)
        except Exception as e:
            if 'Bad Gateway' in str(e):
                llm_wakeup()

    def test_send_single_human_message(self):
        response = send_single_human_message("Hello, how are you?")
        self.assertIsInstance(response, BaseMessage)

    def test_send_human_message_prompt_template(self):
        response = send_human_message_prompt_template("goofy", "Hello, how are you?")
        self.assertIsInstance(response, BaseMessage)

    def test_send_multi_message_prompt_template(self):
        response = send_multi_message_prompt_template("Monty Python", "What is the air speed velocity of a laden swallow?")
        self.assertIsInstance(response, AIMessage)

    def test_send_prompt_with_chat_memory(self):
        response = send_prompt_with_chat_memory("pirate", "How much wood could a woodchuck chuck if a woodchuck could chuck wood?")
        self.assertIsInstance(response, List)
        self.assertIn("woodchuck", response[1].content.lower())


if __name__ == '__main__':
    unittest.main()
