a = 23


class Server:
    def fn1(self):
        pass

    def _fn2(self):
        pass

    def __fn3(self):
        pass


class BackendServer(Server):
    def fn1(self):
        pass

    def _fn2(self):
        pass

    def __fn3(self):
        pass


def __func1(x, y, z):
    total = a + x + y + z

    def inner_func():
        b = total
        print("This is b")

    inner_func()

    return total


def _get_pwd(username):
    # grabs pwd from cloud db
    pass


def _trigger_otp_route(proof):
    # phone number, email
    # grabs pwd from cloud db
    pass


def login(username, password):
    pass


def reset_pwd_not_forgot(username, original_pwd, new_pwd):
    pass


def reset_pwd_forgot(username, new_pwd):
    pass


print(__func1(1, 2, 3))
print(__func1(2, 3, 4))


# private, protected, internal, public
