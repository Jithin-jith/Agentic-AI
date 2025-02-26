#Let's create two conversable agents. 
#We can provide them with system prompts and ask them to play the role of comedians. 
#We can initiate a conversation between them
from autogen import ConversableAgent
from dotenv import load_dotenv
import os
import pprint
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

#Let's create a conversable agent to accomplish a simple task.
#Before doing that we need to set the configuration of the LLM we will use.
llm_config = {
    "model" : "gpt-4o-mini",
    "api_key" : openai_api_key,
    "cache" : None
}
#Let's now define and configure our agents. 
sheldon = ConversableAgent(
    name="sheldon",
    llm_config=llm_config,
    system_message="Your name is Sheldon. You are a well know physicist."
)
penny = ConversableAgent(
    name="penny",
    llm_config=llm_config,
    system_message="Your name is penny. you are a cheerful lady who works at a cheescake factory."
)

#Now let's create a chat between them.
chat = sheldon.initiate_chat(
    recipient=penny,
    message="penny, do you know how stars are formed?",
    max_turns=2
)

#Let's use pretty-print to visualise the entire chat neatly.
pprint.pprint(chat.chat_history) 

"""Openai by defualt assumes that in a conversation there is always a user and an assistant.
ie; it always assume there is a exchange of ideas between an LLM and a user."""

#we can also get the cost associated with this conversation
pprint.pprint(chat.cost)

#We can check the last message of the conversation using the summary method
pprint.pprint(chat.summary)

"""But this is not an actual summary
In-order to get the entire summary we can specify an additional argument to have a real summary of the conversation"""

#Now let's create a chat between them by providing a summary condition as well.
chat = sheldon.initiate_chat(
    recipient=penny,
    message="Penny, do you know how stars are formed?",
    max_turns=2,
    summary_method="reflection_with_llm",#default option is "last_message"
    summary_prompt="summarise the conversation"
)

pprint.pprint(chat.summary)