import os
from typing import List

from langchain.chat_models import AzureChatOpenAI
from langchain.llms import AzureOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, BaseMessage, SystemMessage, AIMessage

api_key = os.environ['OPENAI_API_KEY']
base_url = os.environ['OPENAI_API_BASE']
deployment = os.environ['DEPLOYMENT_NAME']
version = os.environ['OPENAI_API_VERSION']
model = "gpt-35-turbo"


# ------------------------------------------------------------------------------
# TODO Functions - Implement the logic as per instructions
# ------------------------------------------------------------------------------


def send_single_human_message(message) -> AIMessage:
    """
    TODO: Implement this method to create a new AzureChatOpenAI object and invoke the chat object with a List
            containing a single HumanMessage.

    :param:
    message: Takes in user input about what they want to ask the LLM.

    :returns:
    AIMessage object containing the LLM's response.

    Instructions:
    - Create a new AzureChatOpenAI object with the deployment and model variable provided above.
    - Create a new HumanMessage object with the message variable provided above.
    - Send the HumanMessage object to the AzureChatOpenAI object.
    - Return the response from the AzureChatOpenAI object.

    End TODO
    """

    raise NotImplementedError("This function has not been implemented yet.")


def send_human_message_prompt_template(style, message) -> AIMessage:

    """
    TODO: Create a HumanPromptTemplate object from the prompt file, sending the HumanMesasge to the AzureChatOpenAI object
            with the HumanPromptTemplate object's formatted messages.
    :param: 
    style: Takes in user input about what style they AI to respond in. (e.g. cheerful, formal, pirate, etc.)
    message: Takes in user input about what they want to ask the LLM.
    
    :returns: 
    AIMessage object containing the LLM's response.
    
    Instructions:
    - Create a new AzureChatOpenAI object with the deployment and model variable provided above.
    - Create a new HumanMessagePromptTemplate object with the message variable provided above.
    - Send the formatted messages from HumanMessagePromptTemplate object to the AzureChatOpenAI object.
    
    End TODO
    """

    raise NotImplementedError("This function has not been implemented yet.")


def send_multi_message_prompt_template(style, message) -> AIMessage:
    prompt_file = open("../templates/CS_system_prompt.txt")

    """
    TODO: Create a PromptTemplate object using both a HumanMessagePromptTemplate and a SystemMessagePromptTemplate object 
            using the 'CS_system_prompt.txt' from the templates directory.
    
    :param: 
    style: Takes in user input about what style they AI to respond in. (e.g. cheerful, formal, pirate, etc.)
    message: Takes in user input about what they want to ask the LLM.
    
    :returns: 
    AIMessage object containing the LLM's response.
    
    Instructions:
    - Create a new AzureChatOpenAI object with the deployment and model variable provided above.
    - Create a new HumanMessagePromptTemplate object with the message variable provided above.
    - Create a new SystemMessagePromptTemplate object with the style variable provided above.
    - Create a new PromptTemplate object with the HumanMessagePromptTemplate and SystemMessagePromptTemplate objects.
    - Send the formatted messages from PromptTemplate object to the AzureChatOpenAI object.
    
    End TODO
    """

    prompt_file.close()
    raise NotImplementedError("This function has not been implemented yet.")


def send_prompt_with_chat_memory(style, message) -> AIMessage:
    prompt_file = open("../templates/CS_system_prompt.txt")

    """
        TODO: Create a method that utilizes a PromptTemplate object using both a HumanMessagePromptTemplate and a 
                SystemMessagePromptTemplate object using the 'CS_system_prompt.txt' from the templates directory. This 
                method will also use the ConversationBufferMemory object to store the conversation history and send it to
                the LLM.
                

        :param: 
        style: Takes in user input about what style they AI to respond in. (e.g. cheerful, formal, pirate, etc.)
        message: Takes in user input about what they want to ask the LLM.

        :returns: 
        AIMessage object containing the LLM's response.

        Instructions:
        - Create a new AzureChatOpenAI object with the deployment and model variable provided above.
        - Create a new HumanMessagePromptTemplate object with the message variable provided above.
        - Create a new SystemMessagePromptTemplate object with the style variable provided above.
        - Create a new ConversationBufferMemory object.
        - Create a new PromptTemplate object with the HumanMessagePromptTemplate, SystemMessagePromptTemplate, and 
            ConversationBufferMemory objects.
        - Send the formatted messages from PromptTemplate object to the AzureChatOpenAI object.

        End TODO
        """

    prompt_file.close()
    raise NotImplementedError("This function has not been implemented yet.")

# ------------------------------------------------------------------------------
# Starter Code - TOUCH AT YOUR OWN RISK!
# ------------------------------------------------------------------------------

def user_input():
    user_input_style = input("Style: ")
    user_input_message = input("Message: ")

    return [user_input_style, user_input_message]


def main():
    style, message = user_input()
    print(style, message)

    print("#############################Submitting request to Azure Chat OpenAI#####################################")
    print("#########################################################################################################")

    send_single_human_message(message)
    print("#########################################################################################################")
    print("#####################################Single human message completed.#####################################")
    print("#########################################################################################################")
    print()

    send_human_message_prompt_template(style, message)
    print("#########################################################################################################")
    print("#####################################Human message prompt template completed.############################")
    print("#########################################################################################################")
    print()

    send_multi_message_prompt_template(style, message)
    print("#########################################################################################################")
    print("#####################################Multi message prompt template completed.############################")
    print("#########################################################################################################")
    print()

    send_prompt_with_chat_memory(style, message)
    print("#########################################################################################################")
    print("#####################################Prompt with chat memory completed.###################################")
    print()

    print("#########################################################################################################")
    print("############################# END OF REQUEST to Azure Chat OpenAI#####################################")


if __name__ == "__main__":
    main()
