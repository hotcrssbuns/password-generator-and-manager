import secrets
import string


class Password_manager:
    def __init__(self):
        self.pass_length = 12

    def create_password_num_let(self):
        alphabet = string.ascii_letters + string.digits
        password_length = self.pass_length
        return "".join(secrets.choice(alphabet) for i in range(password_length))

    def create_password_num_let_sym(self):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password_length = self.pass_length
        return "".join(secrets.choice(alphabet) for i in range(password_length))
