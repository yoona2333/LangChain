import os
from dotenv import load_dotenv
from langchain_core.messages import content
from langchain_deepseek import ChatDeepSeek
from langchain.agents import create_agent
from langchain_core.tools import tool

load_dotenv()  # 自动加载 .env 文件变量
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
if not deepseek_api_key:
    raise RuntimeError("DEEPSEEK_API_KEY 未配置，请检查 .env 文件")

llm = ChatDeepSeek(model="deepseek-chat", api_key=deepseek_api_key, temperature=0.1)


@tool(description="查询天气信息")
def get_weather() -> str:
    return "明天郑州的天气晴朗"


agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

response = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "明天郑州的天气如何？"}
        ]
    },


)
# print(response)

for message in response["messages"]:
    print(type(message).__name__,message.content)
