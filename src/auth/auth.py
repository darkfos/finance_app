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