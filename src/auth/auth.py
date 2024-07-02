#Local
from src.auth.hash import HashService
from src.db.services.user_service import UserService
from src.db.dto.user_dto import AddNewUser


class Authentication:

    def user_is_created(self, user_data: AddNewUser) -> bool:
        """
        Проверка на существование пользователя
        :param user_data:
        :return:
        """

        find_user: bool = UserService().find_user_by_email(
            email=user_data.email,
            password=HashService().hash_password(password=user_data.password)
        )
        if find_user is False:
            hash_password = HashService().hash_password(password=user_data.password)
            user_data.password = hash_password
            is_created: bool = UserService().add_new(new_user=user_data)
            if is_created:
                return True
            return False
        return False

    def auth_user(self, user_data: AddNewUser) -> bool:
        """
        Проверка данных пользователя
        :param user_data:
        :return:
        """

        #User data
        user_data_from_email: dict = UserService().find_user_auth(email=user_data.email)

        if user_data_from_email:
            is_user_password = HashService().verify(
                password_found=user_data_from_email.get("password"),
                user_password=user_data.password
            )

            if is_user_password:
                return user_data_from_email.get("_id")
            return False

        return False