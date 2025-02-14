from fastapi import FastAPI,status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from datetime import datetime, timezone
from pydantic import BaseModel

class UserResponse(BaseModel):
    email: str
    current_datetime: str
    github_url: str
    class Config:
        orm_mode = True


def init():
    async def lifespan(app:FastAPI):
        yield
    app = FastAPI(title='Fastapi',lifespan=lifespan)
    return app

app = init()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ['*']
)


@app.get('/user',status_code=status.HTTP_200_OK,response_model=UserResponse)
def get_user():
    # Get the current date and time in UTC
    current_datetime_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Format the datetime in ISO 8601 format
    """ iso_8601_utc = current_datetime_utc.isoformat() """
    return {
        "email": "ichekuwilson538@gmail.com",
        "current_datetime": current_datetime_utc,
        "github_url": "https://github.com/Wilsonide/backend-stage0",

        }



if __name__ == "__main__":
    uvicorn.run('main:app',reload=True,port=8000)
