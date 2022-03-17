import uvicorn
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.routes.router import route

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exception):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({"status": '1004'}),
    )


app.include_router(route)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=5556,
    )
