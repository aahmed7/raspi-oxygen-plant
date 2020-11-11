from passlib.hash import pbkdf2_sha256

class Login:
    def get_passwd_hash(self):
        try:
            with open ("userpasswd", "r") as myfile:
                return myfile.read()
        except:
            # Generate default password "password"
            hash = '$pbkdf2-sha256$29000$dc45J4SQ0lrr/b/XGmNMaQ$VDmYehyEzfaDpx0iN4uQShQqgTl.dd/oCiFqR3hpUUE'
            self.set_passwd_hash(hash)
            return hash

    def set_passwd_hash(new_hash):
        with open ("userpasswd", "w") as myfile:
            return myfile.write(new_hash)

    def update_passwd(self):
        new_passwd = input("Enter new password: ")
        hash = pbkdf2_sha256.hash(new_passwd)
        self.set_passwd_hash(hash)

    def check_login_user(self,username,password):
        passwd_hash = self.get_passwd_hash()
        try:
            assert username == "user"
            try:
                assert pbkdf2_sha256.verify(password, passwd_hash)
                print("Login successful.")
                return True
            except:
                print("Wrong Password.")
                return False
        except:
            print("Unknown user.")
            return False