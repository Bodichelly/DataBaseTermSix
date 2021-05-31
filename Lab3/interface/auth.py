from helpers.user_controller import UserController
from main_logic.user_service import user_service
from interface.CUI import CUI
from helpers.console_utils import clear_console


def main(current_user: UserController):
    error_message = "Command not found"
    login_message = "Enter your username: "

    while True:
        choice = CUI.auth_menu()
        if choice == 1:
            clear_console()
            login = input(login_message)
            user_service.register(login)
            current_user.set_current_user_id(user_service.sign_in(login))
            break
        elif choice == 2:
            clear_console()
            login = input(login_message)
            current_user.set_current_user_id(user_service.sign_in(login))
            break
        elif choice == 3:
            quit()
        elif choice == 4:
            print("*** Admin menu activating ***")
            current_user.set_current_user_id(-2)
            break
        else:
            print(error_message)


if __name__ == "__main__":
    main()
