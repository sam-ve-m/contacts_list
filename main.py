from fastapi import FastAPI

from src.infrastructure.mongo import MongoDBInfrastructure
from src.routes.register import route
import uvicorn

from src.services.contact_detail import display_contact_detail

app = FastAPI()
app.include_router(route)

dummy_value = "string:string:0"

print(display_contact_detail(dummy_value, MongoDBInfrastructure.get_singleton_connection()))

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=5555,
    )
