import motor.motor_asyncio

MONGO_DETAILS = "mongodb://mongodb:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.forecast

forecast_collection = database.get_collection("forecast_collection")


#

