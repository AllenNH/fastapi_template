from fastapi import FastAPI
from api.v1.app import router
from api.v1 import  models, schemas
#from db.mongodb import get_mongo_pool, check_mongo_config

app = FastAPI()
 
app = FastAPI(docs_url="/api/v1/docs", openapi_url="/api/v1/auth/openapi.json")
app.include_router(router, prefix="/api/v1")



'''@app.on_event("startup")
async def startup_event():
    logging.info("start up event")
    await check_mongo_config()
@app.on_event("shutdown")
async def shutdown_event():
    logging.info("shutdown event")'''

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)