class UserController:

    def __init__(self, default_id=-1):
        self.current_user_id = default_id

    def get_current_user_id(self) -> int:
        return self.current_user_id

    def set_current_user_id(self, user_id=-1):
        self.current_user_id = user_id

    def is_signed_in(self) -> bool:
        return self.current_user_id != -1 and self.current_user_id != -2

    def is_admin(self) -> bool:
        return self.current_user_id == -2
