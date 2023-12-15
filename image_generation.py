import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
IMAGE_QUEUE = os.getenv('IMAGE_QUEUE')

MAX_QUEUE_ITEMS = 256
MAX_REQUEST_LENGTH = 1024

async def appendToImageQueue(text):
    if len(text) > MAX_REQUEST_LENGTH:
        return False
    
    lock = asyncio.Lock()
    await lock.acquire()

    try:
        with open(IMAGE_QUEUE, 'r') as f:
            num_lines = len(f.readlines())
            if num_lines >= MAX_QUEUE_ITEMS:
                return False
        
        with open(IMAGE_QUEUE, 'a') as f:
            f.write(f'- [ ] {text}\n')
            return True
        
    finally:
        lock.release()