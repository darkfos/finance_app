#System
import os
import dotenv

dotenv.load_dotenv()


class AuthSettings:

    salt: str = os.getenv("SALT")
    api_course_value_key: str = os.getenv("API_COURSE_VALUE_KEY")
    url_course_value: str = os.getenv("URL_API_COURSE_VALUE")