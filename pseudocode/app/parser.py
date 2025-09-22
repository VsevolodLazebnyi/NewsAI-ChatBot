import time
import logging
import datetime
import pytz
import typing
import os
import re
import faiss
import numpy as np
import apscheduler
import signal
import sys

# Псевдокод / Pseudocode

db = Database()

def delete_old_entries():
    
def clean_digest(text):

def create_digests_for_categories():

def save_news_to_db(news_list):

def determine_news_category(title, content):

def main():
    start_time = datetime.now()
    sources = list(db.source_collection.find({}))
    for source in sources:
        try:
            news = get_all_news(source)
            if news:
                save_news_to_db(news)
            else:
                logger.warning(f"")
        except Exception as e:
            logger.error(f"")

    duration = (datetime.now() - start_time).total_seconds()
    create_digests_for_categories()
    drop_bad_summaries()
    duration_digests = (datetime.now() - start_time).total_seconds()        
   

if __name__ == "__main__":
    scheduler = BlockingScheduler(timezone="Europe/Moscow")
    scheduler.add_job(main, trigger=CronTrigger(hour="0,6", minute=0), name="Night parsing")
    scheduler.add_job(main, trigger=CronTrigger(hour="7-22/3", minute=30), name="Day parsing")
    scheduler.start()