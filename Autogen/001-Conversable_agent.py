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
}

#Let's configure a conversable agent that will use the above llm config and will never ask our input
agent = ConversableAgent(
    name="chatbot",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

#Let's now send a prompt to this agent and get a reply.
response = agent.generate_reply(
    messages=[
        {"role":"user","content":"Tell me a fun fact about money."}
    ]
)
print(response)

#Now let's try to ask this agent something that refers to the last query.
response = agent.generate_reply(
    messages=[
        {"role":"user","content":"Repeat the fact."}
    ]
)
print(response)
#It always generate a new reply.But we need to keep the state to be able to solve complex tasks.