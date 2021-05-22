import atexit as at_exit

from interface.admin import main as admin
from interface.auth import main as auth
from interface.common import main as common

from helpers.user_controller import UserController
from main_logic.user_service import user_service


def main():
    current_user = UserController()

    def exit_handler():
        if current_user.is_signed_in():
            user_service.sign_out(current_user.get_current_user_id())

    at_exit.register(exit_handler)

    while True:
        if current_user.is_admin():
            admin(current_user)
        elif not current_user.is_signed_in():
            auth(current_user)
        else:
            common(current_user)


if __name__ == "__main__":
    main()
