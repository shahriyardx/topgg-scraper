import asyncio
import os

import hypercorn
from dotenv import load_dotenv
from hypercorn.asyncio import serve

from main import app

load_dotenv(".env")

HOST = os.getenv("HOST", "localhost")
PORT = os.getenv("PORT", "5000")

config = hypercorn.Config()
config.bind = [f"{HOST}:{PORT}"]

asyncio.run(serve(app, config))
