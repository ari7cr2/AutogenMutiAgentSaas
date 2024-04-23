#start server in LMStudio (port 1234)

from autogen import AssistantAgent, GroupChatManager, UserProxyAgent
from autogen.agentchat import GroupChat

config_list = [
    {
        "api_base": "http://localhost:1234/v1", #for lmstudio server
        "api_type": "open_ai",
        "api_key": "NULL",
    }
]

llm_config = {"config_list": config_list, "seed": 42, "request_timeout": 600,
              "temperature": 0,}