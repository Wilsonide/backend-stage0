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

-----BEGIN RSA PRIVATE KEY-----
MIIEpgIBAAKCAQEA7An9hsffUwu4TiF166VVsPSrDWXIXk/AwgmiIFpPAOpjLmNe
qPbvNG+v6VLa5Ub5XMOXMmn8ghYpGv4xN/A0K7nLKaLNw7UXh3uKx5NViPrtgJvd
DScY6riANX1gcPK92RL27icB06QCPlFJhd7fXXLvhw/nuyaQgNN/IfPBlIgA3HJh
iSiRj1QVfW7T81SOH4mVLDwG1TSStAEypUWbftxGsPenM49LkIjiE+rTyyU1S03h
4lEc2L58w/qNXkNE+AFU7cMYY97gIiJkJJ0VNoWFKawlHZo1J0ZLDP3qDKSqc+4F
oM2AcEq/o0INpZ8dLMPHEV49sBkbEtB5Zj0PLQIDAQABAoIBAQCaRnFZrbvO2MMu
9fnP+nGGxnQivpr24aO4b3lzMfOfQpNu124ge72fBTzyAMCnyPrlYcWqItHy6K8X
QHtE94/x4G7kmM9qkit91wa/KRJoBLJFNBqIJTzI9ax+yaLGUDI79oRE5mPwQ6tf
tdubTy+pMZ1TJtcsYKlkOlhHBb5J6FU80VyaFggQ8XkJHWqbeS1IuCkzZkxvx3/m
/Ufg6mKe6lVEVJSjoMM//FVsSYIz9qVkEqNpzx7F//AcV96gtF9rfKyF+BJH1Ww5
mKUYKn5si24aWPAUXSNvtIN/anA73F0/izjirOR7aIgKUP5CWK/E9dsNvVq59BhO
sJO7hZUBAoGBAP4NU+z7AGaUO1TD20ZY2BLhQTlF1n/PWj565UVEzARUIwh39cbC
S9Pf7uX14SjyP5toZsE7g2xSfB9WLy+YloMGi7T2ObNC3fNa2gdoRw4FjvP+1xQS
0grFPnThosbE367uYhPf1ytwWV/NMXWXWTHxiq9wPg3Pb5HQqGJbE51BAoGBAO3Z
TiBvOyqAvPqiBs3ZxBGFYahb5WHKDyN4cjQi8jWbImcv5OpIy3e7sjwV0hJfvOAr
tRocVqvvEECDZjct0egCA3ssGIRSB6wEkM9uKTOPWwntnx1n0Mdd1Fk4gq+WRawQ
0YBYho3Yf5ey3pX3y87VYAXKzYfD1stGd17lw/rtAoGBAP1fqX5Gb4Xe/LVziLPG
U+mwgm5uepmJ4cVCqHrHPHpst2vwyEzs5tdvFUKAUYmW4V1LaH/7rP1R3r0aJYFg
u2v+EUPv9mgUnmvhBmYw1/ziCkrKtRMuGhHn2nyTtNZs73H2ChcsPdry+BAWA+f1
hF3NOrXySdFYOzvAUM+Xah6BAoGBAIIBm3CjG+X5hFJCqhFujHs/Osf5owG2nlu3
BEV3LIkciMt6JFfi/kQt9hhdnPuqFOU7PrxM7RsBixKYQBC9HNUB9MEosyXwaH0f
6b9X6XFjVFGy7pv2GOpAYUd7WgN70g1hDAJpYPK7edKDVKMIVQBzJQ9FcN5ar1dg
5vKaCGtpAoGBAM5I5g0o/QefKFN6nowPwZxZ1jgREERCejEQRImZYYpiVQvqRzJc
94UxugHPSdEv/rnDEnPxFYaErbpm6F9vpAmPvEvgAmb1Klfxqk+BsbjgBxVkxkhE
oVlUN4oZ+loRanulH0cGyq5Va2lLYMCoc3j+oIdDllspDNdkTqM+hctm
-----END RSA PRIVATE KEY-----


if __name__ == "__main__":
    uvicorn.run('main:app',reload=True,port=8000)
