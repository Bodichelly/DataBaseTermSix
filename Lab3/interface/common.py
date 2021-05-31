from helpers.user_controller import UserController
from main_logic.user_service import user_service, print_messages_statistics
from interface.CUI import CUI
from helpers.console_utils import clear_console

def main(current_user: UserController):
    error_message = "Command not found"

    while True:
        choice = CUI.common_user_menu()

        if choice == 1:
            clear_console()
            message = input("Write message text: ")
            receiver = input("Enter username you want to send message: ")

            if user_service.create_message(message, current_user.get_current_user_id(), receiver):
                print("*** Sending message ***")
        elif choice == 2:
            clear_console()
            user_service.print_messages(current_user.get_current_user_id())
        elif choice == 3:
            clear_console()
            print_messages_statistics(current_user.get_current_user_id())
        elif choice == 4:
            clear_console()
            user_service.sign_out(current_user.get_current_user_id())
            current_user.set_current_user_id()
            break
        else:
            print(error_message)


if __name__ == "__main__":
    main()
