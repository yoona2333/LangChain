import streamlit as st
from dashscope.cli.files import upload

from RAG项目.konowledge_base import KnowledgeBaseService

st.title("知识库更新")

upload_file = st.file_uploader(
    "请上传txt文件",
    type=['txt'],
    accept_multiple_files=False,  # 仅接受一个文件的上传
)

if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()


if upload_file is not None:
    file_name = upload_file.name  # 文件名
    file_type = upload_file.type  # 文件类型
    file_size = upload_file.size / 1024  # 文件大小

    st.subheader(f"文件名:{file_name}")

    st.write(f"格式：{file_type}| 大小：{file_size:.2f} KB")

    text=upload_file.getvalue().decode("utf-8")

    st.session_state["service"].upload_by_str(text, file_name)
    # st.write(text)

    # st.session_state["count"] += 1  # 上传文件后，计数加1



