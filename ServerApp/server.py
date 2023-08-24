from fastapi import FastAPI, HTTPException, Depends, Request
import numpy as np
from typing import List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import security
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Configure CORS settings
origins = [
    "http://localhost",    # Add the list of allowed origins
    "http://localhost:8651",  # Example: a frontend app running on localhost
    "http://localhost:8650",
    "http://10.113.34.11",
    "http://10.113.34.11:8651"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can restrict the HTTP methods if needed
    allow_headers=["*"],  # You can restrict the headers if needed
)


@app.get("/")
async def read_index(request: Request):
    """
    this command tells the status of server
    """
    return {
        "status" : "Up and Running!"
    }

@app.get("/vectorize")
async def vectorizeString(user_input : str, 
                          token: str = Depends(oauth2_scheme)
                          ) -> List[float]:
    """method to vectorize input string 

    Args:
        user_input (str): input string to be vectorized
        token (str, optional): _description_. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: 422 (Unprocessable Entity)

    Returns:
        List[float]: 500-dimension vector
    """
    if (len(user_input) <= 25):
        raise HTTPException(
            status_code=422, 
            detail="Unprocessable Input! User input must be lengthier than 25 characters."
        )
    else:
        vect_rep = [np.round(i,5) for i in list(np.random.rand(500))]
        return {
            "user_input" : user_input,
            "vector_representation" : vect_rep
        }
    
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """login API for getting OATH2 token

    Args:
        form_data (OAuth2PasswordRequestForm, optional): form_data containing username and password details entered by user.

    Raises:
        HTTPException: 400 for incorrect username and password or when user doesn't exists in database
        
    Returns:
        json object : it returns access_token that needs to be appended to subsequent API calls
    """
    # print(form_data.username)
    user_dict = security.fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = security.UserInDB(**user_dict)
    hashed_password = security.fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}