from util.keys import initial

# 初始化秘钥配置
initial()

from langchain.chat_models import PromptLayerChatOpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType

llm = PromptLayerChatOpenAI(temperature=0.0, pl_tags=["test-06"])
math_llm = PromptLayerChatOpenAI(temperature=0.0, pl_tags=["test-06"])
tools = load_tools(
    ["human", "llm-math"],
    llm=math_llm,
)

agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

agent_chain.run("What's my friend Eric's surname?")
# Answer with 'Zhu'
