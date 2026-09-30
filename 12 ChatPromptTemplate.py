# 核心组件导入
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # 聊天模板 + 消息占位符
from langchain_core.runnables import RunnableSerializable                  # 可运行序列类型标注
from langchain_ollama import ChatOllama                                    # Ollama 本地大模型封装



# 构建聊天提示模板：系统角色 + 历史占位符 + 当前用户输入
# MessagesPlaceholder("history") 运行时会被 history 参数的消息列表替换
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个边塞诗人，可以作诗。"),  # 系统提示，设定 AI 身份
        MessagesPlaceholder("history"),             # 多轮对话历史占位符
        ("human", "请再来一首唐诗"),                  # 当前用户提问
    ]
)

# 模拟的多轮对话历史，运行时注入到 MessagesPlaceholder 位置
history_data = [
    ("human", "你来写一个唐诗"),
    ("ai", "床前明月光，疑是地上霜，举头望明月，低头思故乡"),
    ("human", "好诗再来一个"),
    ("ai", "锄禾日当午，汗滴禾下锄，谁知盘中餐，粒粒皆辛苦"),
]

# 调试用：模板渲染为纯字符串，查看最终 prompt 效果
# prompt_text = chat_prompt_template.invoke({"history": history_data}).to_string()

# 初始化 Ollama 本地模型
# model: Ollama 中已拉取的模型名；base_url: Ollama 本地服务地址
model = ChatOllama(
    model="qwen3-vl:4b",
    base_url="http://localhost:11434",
)


# LCEL 链式调用：提示模板 → 大模型
chain: RunnableSerializable = chat_prompt_template | model

# 方式一：invoke 同步调用，等待模型完整生成后一次性返回
res = chain.invoke({"history": history_data})

# 方式二：stream 流式调用，逐 token 产出并实时打印输出
ress = chain.stream({"history": history_data})
for r in ress:
    if r.content:
        print(r.content, end="", flush=True)  # end="" 不换行，flush=True 立即刷新

# print(res.content, type(res))