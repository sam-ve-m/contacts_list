from fastapi import FastAPI

router = FastAPI()


@router.post("/register")
def register_contact():
    pass
