from fastapi import FastAPI

app = FastAPI(openapi_prefix="/g3")


@app.post("/register")
def register_contact():
    pass

