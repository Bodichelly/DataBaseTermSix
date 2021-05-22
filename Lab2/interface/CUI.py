from helpers.console_utils import console_divider


class CUI:
    choiceMessage = "Choose your next action: "

    @staticmethod
    def auth_menu() -> int:
        console_divider()
        print("[1] Register")
        print("[2] Login")
        print("[3] Exit")
        return int(input(CUI.choiceMessage))

    @staticmethod
    def common_user_menu() -> int:
        console_divider()
        print("[1] Send message")
        print("[2] My messages")
        print("[3] Statistic")
        print("[4] Logout")
        return int(input(CUI.choiceMessage))

    @staticmethod
    def admin_menu() -> int:
        console_divider()
        print("[1] Users online")
        print("[2] Top senders")
        print("[3] Top spammers")
        print("[4] Exit")
        return int(input(CUI.choiceMessage))