from fastapi import FastAPI

#引入api实例
app = FastAPI()

@app.get("/")
def root():
    return "hello world"


@app.get("/user")
def get_users():
    list=[
        {"id" : 1, "name" : "张三"},
        {"id" : 2, "name" : "张三"},
        {"id" : 3, "name" : "张三"},
    ]
    return list

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)

