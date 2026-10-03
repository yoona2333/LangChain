md5_path="./md5.txt"

collect_name="rag"
persist_directory="./chroma_db"

chunk_size=1000
chunk_overlap=100
separators=["\n\n", "\n", " ", "","!","?",""]

max_split_char_number=1000 # 分段最大字符数，超过1000个字符进行分段

similarity_threshold=2 # 相似度阈值，超过3个文档，认为是相似的




