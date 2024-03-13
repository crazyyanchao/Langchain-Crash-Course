from util.keys import initial

# ===========================初始化秘钥配置===========================
initial()

from langchain.agents import create_csv_agent
from langchain.chat_models import PromptLayerChatOpenAI

agent = create_csv_agent(PromptLayerChatOpenAI(pl_tags=["csv-qa"], temperature=0),
                         'managers.csv',
                         verbose=True)

agent.run("男性高管有多少位？")


# agent.run("文件有多少列？") Final Answer: 11
# agent.run("文件有多少行？") Final Answer: 232156

