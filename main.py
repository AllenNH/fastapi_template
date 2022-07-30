from fastapi import FastAPI
from api.v1.app import router
from api.v1 import  models, schemas

app = FastAPI()
 
app = FastAPI(docs_url="/api/v1/docs", openapi_url="/api/v1/auth/openapi.json")
app.include_router(router, prefix="/api/v1")