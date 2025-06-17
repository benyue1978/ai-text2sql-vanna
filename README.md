# Vanna Text2SQL 示例项目

本项目演示如何用Vanna实现text2sql，并连接本地SQLite数据库。

## 安装依赖

```bash
pip install -r requirements.txt
```

## 初始化数据库

```bash
python init_db.py
```

## 运行主程序（命令行示例）

请先设置你的OpenAI API Key（推荐用.env）：

```bash
cp .env.example .env
#修改.env中的key
python vanna_text2sql.py
```

## 启动Web界面

```bash
python vanna_text2sql.py
```

访问 <http://localhost:8084> 用网页体验text2sql。

---

如需自定义表结构或训练数据，请修改`init_db.py`和`vanna_text2sql.py`。
