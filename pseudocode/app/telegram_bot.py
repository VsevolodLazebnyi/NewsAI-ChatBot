import logging
import os
import re
import asyncio
import aiogram 
from datetime import datetime, timedelta
import apscheduler


# Псевдокод / Pseudocode

scheduler = AsyncIOScheduler()
async def main():
    try:
        if not scheduler.running:
            scheduler.start()
        users = db.user_collection.find()
        for user in users:
            user_id = user["_id"]
            schedule = user.get("schedule", {})
            if schedule.get("enabled", True):
                times = schedule.get("times", ["12:00"])
                schedule_user_digests(user_id, times)
                user_count += 1
        await dp.start_polling(bot)
    except Exception as e:
        raise


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    scheduler.shutdown()
    loop.close()