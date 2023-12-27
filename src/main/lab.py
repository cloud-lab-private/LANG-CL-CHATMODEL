import os
from typing import List

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.prompts import HumanMessagePromptTemplate, SystemMessagePromptTemplate, ChatPromptTemplate, \
    MessagesPlaceholder

llm = HuggingFaceEndpoint(
    endpoint_url="https://z8dvl7fzhxxcybd8.eu-west-1.aws.endpoints.huggingface.cloud",
    huggingfacehub_api_token="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",
    task="text2text-generation",
    model_kwargs={
        "max_new_tokens": 200
    }
)

# ------------------------------------------------------------------------------
# TODO Functions - Implement the logic as per instructions
# ------------------------------------------------------------------------------


def send_single_human_message(message) -> BaseMessage:
    """
    TODO: Implement this method to create a new AzureChatOpenAI object and invoke the chat object with a List
            containing a single HumanMessage.

    :param:
    message: Takes in user input about what they want to ask the LLM.

    :returns:
    AIMessage object containing the LLM's response.

    Instructions:
    - Create a new AzureChatOpenAI object with the model variable provided above.
    - Create a new HumanMessage object with the message variable provided above.
    - Send the HumanMessage object to the AzureChatOpenAI object.
    - Return the response from the AzureChatOpenAI object invoke method.

    End TODO
    """
    # Write Code Below
    chat_model = ChatHuggingFace(llm=llm)
    response = chat_model.invoke([HumanMessage(content=message)])
    return response

    # Replace with return statement
    # raise NotImplementedError("This function has not been implemented yet.")


def send_human_message_prompt_template(style, message) -> BaseMessage:
    """
    TODO: Create a HumanPromptTemplate object from the prompt file, sending the HumanMesasge to the AzureChatOpenAI object
            with the HumanPromptTemplate object's formatted messages.
    :param: 
    style: Takes in user input about what style they AI to respond in. (e.g. cheerful, formal, pirate, etc.)
    message: Takes in user input about what they want to ask the LLM.
    
    :returns: 
    AIMessage object containing the LLM's response.
    
    Instructions:
    - Create a new AzureChatOpenAI object with the model variable provided above.
    - Create a new HumanMessagePromptTemplate object with the message variable provided above.
    - Send the formatted messages from HumanMessagePromptTemplate object to through the invoke method of the AzureChatOpenAI object.
    - Return the response from the AzureChatOpenAI object.
    
    End TODO
    """
    # Write Code Below
    chat_model = ChatHuggingFace(llm=llm)
    human_message = HumanMessagePromptTemplate.from_template(message)
    response = chat_model.invoke([human_message.format()])
    return response
    # Replace with return statement
    # raise NotImplementedError("This function has not been implemented yet.")


def send_multi_message_prompt_template(style, message) -> BaseMessage:
    # System message prompt template
    file = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../templates/system_prompt.txt')))
    prompt_file = file.read()
    file.close()

    """
    TODO: Create a PromptTemplate object using both a HumanMessagePromptTemplate and a SystemMessagePromptTemplate object 
            using the 'system_prompt.txt' from the templates directory.
    
    :param: 
    style: Takes in user input about what style they AI to respond in. (e.g. cheerful, formal, pirate, etc.)
    message: Takes in user input about what they want to ask the LLM.
    
    :returns: 
    AIMessage object containing the LLM's response.
    
    Instructions:
    - Create a new AzureChatOpenAI object with model variable provided above.
    - Create a new HumanMessagePromptTemplate object with the message variable provided above.
    - Create a new SystemMessagePromptTemplate object with the prompt_file variable provided above.
    - Create a new ChatPromptTemplate object with the HumanMessagePromptTemplate and SystemMessagePromptTemplate objects.
    - Send the formatted messages from PromptTemplate object to the AzureChatOpenAI object via the invoke method, returning 
        the Message from the AI.
    
    End TODO
    """
    # Write Code Below
    chat_model = ChatHuggingFace(llm=llm)
    human_message = HumanMessagePromptTemplate.from_template(message)
    system_message = SystemMessagePromptTemplate.from_template(prompt_file)
    chat_prompt = ChatPromptTemplate.from_messages([human_message, system_message])
    response = chat_model.invoke(chat_prompt.format())
    return response

    # Replace with return statement
    # raise NotImplementedError("This function has not been implemented yet.")


def send_prompt_with_chat_memory(style, message) -> List[BaseMessage]:
    system_ai_template = f"An AI that is here to help any human to answer any questions. Talks in a {style} tone."
    message2 = "What can birds do?"
    message3 = "How many messages have we exchanged? About what?"

    """
    TODO: The send_prompt_with_chat_memory function is designed to facilitate a conversation with the Language 
    Learning Model (LLM). It creates an AzureChatOpenAI object and a ChatPromptTemplate object, which includes a 
    SystemMessagePromptTemplate, a MessagesPlaceholder for history, and a HumanMessagePromptTemplate. The function 
    also initializes a ConversationBufferMemory object to store the conversation history. It then creates a 
    ConversationChain object and sends messages through the run method. Finally, it returns the conversation 
    history.

    :param: 
    style: Takes in user input about what style they AI to respond in. (e.g. cheerful, formal, pirate, etc.)
        message: Takes in user input about what they want to ask the LLM.

    :returns: 
    AIMessage object containing the LLM's response.

    Instructions:
        - Create a new AzureChatOpenAI object with the model variable provided above.
        - Create a new ChatPromptTemplate object using the from_messages method with a List contain a SystemMessagePromptTemplate object,
            a MessagesPlaceholder object with the 'history' value, and a HumanMessagePromptTemplate object.
        - Create a new ConversationBufferMemory object.
        - Create a new ConversationChain object with the AzureChatOpenAI object for the 'llm' value, the ChatPromptTemplate
            object for the 'prompt' value, and the ConversationBufferMemory object for the 'memory' value in the chain.
        - Using the ConversationChain object, send each message through the predict method. Inputting each message object:
            message, message2 and message3.
        - By using ConversationBufferMemory object's load_memory_variables method, we return an dictionary that contains
            a key for 'history'. Extract & Return the value for the 'history' key, which is our List[BaseMessage] object.

    End TODO
    """
    # Write Code Below
    chat_model = ChatHuggingFace(llm=llm)
    chat_prompt = ChatPromptTemplate.from_messages(
        [SystemMessagePromptTemplate.from_template(system_ai_template), MessagesPlaceholder("history"),
         HumanMessagePromptTemplate.from_template(message)])
    conversation_buffer = ConversationBufferMemory()
    conversation_chain = ConversationChain(llm=chat_model, prompt=chat_prompt, memory=conversation_buffer)
    conversation_chain.predict([message, message2, message3])
    return conversation_buffer.load_memory_variables()['history']

    # Replace with return statement
    # raise NotImplementedError("This function has not been implemented yet.")
