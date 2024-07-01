#System
import os
import dotenv

dotenv.load_dotenv()


class AuthSettings:

    salt: str = os.getenv("SALT")
    api_course_value_key: str = os.getenv("API_COURSE_VALUE_KEY")
    api_coin_value_key: str = os.getenv("API_COIN_KEY")
    url_course_value: str = os.getenv("URL_API_COURSE_VALUE")
    url_course_coin: str = os.getenv("URL_API_COIN")