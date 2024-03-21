# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr

import motor.motor_asyncio
from config import Rkn_Bots

client = motor.motor_asyncio.AsyncIOMotorClient(Rkn_Bots.DB_URL)
db = client.captions_with_chnl
chnl_ids = db.chnl_ids
users = db.users

# Total User
async def total_user():
    user = users.count_documents({})
    return user

async def getid():
    all_users = users.find({})
    return all_users

async def delete(id):
    users.delete_one(id)
                     
async def addCap(chnl_id, caption):
    dets = {"chnl_id": chnl_id, "caption": caption}
    await chnl_ids.insert_one(dets)

async def updateCap(chnl_id, caption):
    await chnl_ids.update_one({"chnl_id": chnl_id}, {"$set": {"caption": caption}})

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr