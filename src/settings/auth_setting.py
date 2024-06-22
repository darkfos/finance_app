import os
import dotenv

dotenv.load_dotenv()


class AuthSettings:

    salt: str = os.getenv("SALT")