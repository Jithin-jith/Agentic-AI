#up intill now we were just terminating the chat using the max_turns condition.
#now let's define a termination condition within the chat/conversation.

from autogen import ConversableAgent
from dotenv import load_dotenv
import os
import pprint
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

#Let's create two conversable agent to initiate a conversation.
#Before doing that we need to set the configuration of the LLM we will use.
llm_config = {
    "model" : "gpt-4o-mini",
    "api_key" : openai_api_key,
    "cache" : None
}
sheldon = ConversableAgent(
    name="sheldon",
    llm_config=llm_config,
    system_message="Your name is Sheldon. You are a well know physicist rushing to work." + 
    "when you are done with the conversation say 'I gotta go'. ",
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "I gotta go" in msg["content"]
)
penny = ConversableAgent(
    name="penny",
    llm_config=llm_config,
    system_message="Your name is penny. you are a cheerful lady who works at a cheescake factory." +
    "when you are done with the conversation say 'I gotta go'. ",
    is_termination_msg=lambda msg: "I gotta go" in msg["content"]
)
#Now let's initiate a chat between them.
chat = sheldon.initiate_chat(
    recipient=penny,
    message="penny, do you know how stars are formed?"
)

