from main_logic.worker import main as Worker
from helpers.user_controller import UserController
from helpers.console_utils import clear_console
from helpers.redis_set_up import connection
from interface.CUI import CUI


def main(current_user: UserController):
    error_message = "Command not found"

    while True:
        choice = CUI.admin_menu()

        if choice == 1:
            clear_console()
            online_users = connection.smembers("online:")
            print("Users online:")
            for index, user in enumerate(online_users):
                print(f"{index + 1}. {user}")

        elif choice == 2:
            clear_console()
            senders = connection.zrange("sent:", 0, 4, desc=True, withscores=True)
            print("Top senders:")
            for index, sender in enumerate(senders):
                username = sender[0].replace("user:", "")
                messages_count = sender[1]
                print(f"{index + 1}. {username}: {int(messages_count)} messages")

        elif choice == 3:
            clear_console()
            spammers = connection.zrange("spam:", 0, 4, desc=True, withscores=True)
            print("Top spammers:")
            for index, spammer in enumerate(spammers):
                username = spammer[0].replace("user:", "")
                messages_count = spammer[1]
                print(f"{index + 1}. {username}: {int(messages_count)} messages")
        elif choice == 4:
            current_user.set_current_user_id()
            break
        else:
            print(error_message)


if __name__ == '__main__':
    main()