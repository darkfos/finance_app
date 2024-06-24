#System
import os
from dotenv import load_dotenv


load_dotenv()


class DatabaseSettings:

    db_url: str = os.getenv("MONGO_CONNECTED_URL")