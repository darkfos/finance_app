#Other libraries
import flet


#Local
from src.app.router import Router
from src.session import UserSession


if __name__ == "__main__":
    #Точка входа

    flet.app(target=Router)