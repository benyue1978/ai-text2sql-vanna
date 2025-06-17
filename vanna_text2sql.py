from vanna.openai.openai_chat import OpenAI_Chat
from vanna.chromadb.chromadb_vector import ChromaDB_VectorStore
from vanna.flask import VannaFlaskApp
import os
from dotenv import load_dotenv

# 加载.env文件
load_dotenv()

# 从环境变量获取OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# 指定chroma和其它vanna临时文件目录
VN_TEMP_DIR = "vanna_tmp"
os.makedirs(VN_TEMP_DIR, exist_ok=True)

class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)

vn = MyVanna(config={
    'api_key': OPENAI_API_KEY,
    'model': 'gpt-3.5-turbo',
    'path': os.path.join(VN_TEMP_DIR, "chroma")  # chroma向量库目录
})

# 连接本地sqlite数据库
vn.connect_to_sqlite('mydb.sqlite')

# 训练：让Vanna了解表结构
print('正在训练表结构...')
df_ddl = vn.run_sql("SELECT sql FROM sqlite_master WHERE type='table'")
for ddl in df_ddl['sql'].to_list():
    vn.train(ddl=ddl)

# 添加业务文档和示例SQL
vn.train(documentation="users表存储了用户的姓名和年龄")
vn.train(question="查询所有用户的姓名和年龄", sql="SELECT name, age FROM users")

# 示例：用自然语言提问
print('自然语言查询示例：')
result = vn.ask("30岁以上的用户有哪些？")
print(result)

# 可选：启动Web界面
if __name__ == "__main__":
    app = VannaFlaskApp(vn, allow_llm_to_see_data=True)
    app.run() 