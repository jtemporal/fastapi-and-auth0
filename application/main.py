"""FastAPI starter sample: Protected endpoint
"""

from fastapi import Depends, FastAPI, Response, status
from fastapi.security import HTTPBearer

from .utils import VerifyToken


# Scheme for the Authorization header
token_auth_scheme = HTTPBearer()

app = FastAPI()


@app.get("/api/public")
def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": ("Hello from a public endpoint! "
                "You don't need to be authenticated to see this.")
    }
    return result


@app.get("/api/private")
def private(response: Response, token: str = Depends(token_auth_scheme)):
    """A valid access token is required to access this route"""

    result = VerifyToken(token.credentials).verify()

    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    return result
