import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek

load_dotenv()  # 自动加载 .env 文件变量 ，环境变量
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")  # 获取环境变量中的 DEEPSEEK_API_KEY


@tool(description="查询股票价格")
def get_price(name: str) -> str:
    return f"股票{{name}}的价格是100元"


@tool(description="查询股票信息")
def get_info(name: str) -> str:
    return f"股票{{name}}的信息是一家上市公司，专注于it教育"


agent = create_agent(
    model=ChatDeepSeek(
        model="deepseek-chat",
        api_key=deepseek_api_key,
        temperature=0.1
    ),
    tools=[get_price, get_info],
    system_prompt="You are a helpful assistant，可以回答股票价格和股票信息，记得告诉我你的思考过程，让我知道你为什么调用",
)
# 控制随机性，0.1 表示较低的随机性 作用是让生成结果更确定 - **越接近 0**：模型越保守、确定，每次相同提问得到的回答差别很小，**不容易瞎编（幻觉少）**，适合 RAG 知识库问答、数据查询、事实类问题。

# 你的 0.1就属于这一档，很适合你的尺码知识库问答场景。
# 越接近 1：创造性变强，回答更多样，适合写文案、润色、创意写作。
# 大于 1：发散性极强，脑洞大，回答不稳定，容易胡编，RAG 场景不要用。

for chunk in agent.stream(
        {
            "messages": [{"role": "user", "content": "股票阿里巴巴的价格是多少,并介绍一下?"}],

        },
        stream_mode="values"
):
    # print(chunk["messages"][-1].content)

    last_message=chunk["messages"][-1] # 获取最后一个消息

    if last_message.content:
        print(last_message.content, type(last_message).__name__)
    try:
        if last_message.tool_calls:
            print(f"Tool Call: {[tc['name'] for tc in last_message.tool_calls]}")
    except AttributeError as e:
        pass

