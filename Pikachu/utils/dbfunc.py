from Pikachu.mongo import db
from Pikachu.utils.dbfunc import (update_karma, get_karma, get_karmas,
from Pikachu.utils.dbfunc import (get_couple, save_couple,


# Couple Chooser

async def _get_lovers(chat_id: int):
    lovers = coupledb.find_one({"chat_id": chat_id})
    if lovers:
        lovers = lovers["couple"]
    else:
        lovers = {}
    return lovers


async def get_couple(chat_id: int, date: str):
    lovers = await _get_lovers(chat_id)
    if date in lovers:
        return lovers[date]
    else:
        return False


async def save_couple(chat_id: int, date: str, couple: dict):
    lovers = await _get_lovers(chat_id)
    lovers[date] = couple
    await coupledb.update_one(
        {"chat_id": chat_id},
        {
            "$set": {
                "couple": lovers
            }
        },
        upsert=True
    )
