import os
import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv(verbose=True)

class Mongo(object):
    _mongo = None
    @classmethod
    async def create_mongo_pool(cls):
        if not cls._mongo:
            #mongo_url = os.getenv("DB_HOST")
            mongo_url = "url"
            logging.info(f"Connecting to mongo at {mongo_url}")
            cls._mongo =  motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
            
        return cls._mongo


async def get_mongo_pool():
    mongo = await Mongo.create_mongo_pool()
    
    return mongo

async def check_mongo_config():
    mongo = await Mongo.create_mongo_pool()
    if(dict(await mongo.test.md.index_information()).get("key",0) == 0):
        await mongo.test.md.create_index([("entity_type", 1),("entity_id", 1)], name="key", unique = True)
    return mongo