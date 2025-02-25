#Let's create two conversable agents. 
#We can provide them with system prompts and ask them to play the role of comedians. 
#We can initiate a conversation between them
from autogen import ConversableAgent
from dotenv import load_dotenv
import os
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
