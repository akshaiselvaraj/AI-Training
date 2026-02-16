class Auth:
    def login(self): pass

class PasswordAuth(Auth):
    def login(self):
        print("Password verified")

class OTPAuth(Auth):
    def login(self):
        print("OTP verified")

a = OTPAuth()
a.login()
