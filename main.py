from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    """
    注册一个根路径
    :return:
    """
    return {"message": "Hello World"}


@app.get("/info")
async def info():
    """
    项目信息
    :return:
    """
    return {
        "app_name": "FastAPI框架学习",
        "app_version": "v0.0.1"
    }

# 测试使用
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
