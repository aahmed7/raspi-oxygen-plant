from passlib.hash import pbkdf2_sha256
import stdiomask

class Login:
    """This class contains methods for directly interacting with the sensors.

    Attributes:
        login: login status
    """

    def set_passwd_hash(self,new_hash):
        '''
        Initialize the ADC

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        with open ("userpasswd", "w") as myfile:
            return myfile.write(new_hash)

    def set_adm_passwd_hash(self,new_hash):
        '''
        Initialize the ADC

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        with open ("adminpasswd", "w") as myfile:
            return myfile.write(new_hash)

    def get_passwd_hash(self):
        '''
        Initialize the ADC

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        try:
            with open ("userpasswd", "r") as myfile:
                return myfile.read()
        except:
            # Generate default password "passwd"
            hash = '$pbkdf2-sha256$29000$dc45J4SQ0lrr/b/XGmNMaQ$VDmYehyEzfaDpx0iN4uQShQqgTl.dd/oCiFqR3hpUUE'
            self.set_passwd_hash(hash)
            return hash

    def get_adm_passwd_hash(self):
        '''
        Initialize the ADC

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        try:
            with open ("adminpasswd", "r") as myfile:
                return myfile.read()
        except:
            # Generate default password "passwd"
            hash = '$pbkdf2-sha256$29000$dc45J4SQ0lrr/b/XGmNMaQ$VDmYehyEzfaDpx0iN4uQShQqgTl.dd/oCiFqR3hpUUE'
            self.set_passwd_hash(hash)
            return hash

    def update_passwd(self):
        '''
        Initialize the ADC

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        new_passwd = input("Enter new password: ")
        hash = pbkdf2_sha256.hash(new_passwd)
        self.set_passwd_hash(hash)

    def check_login_user(self):
        '''
        check_login_user

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        passwd_hash = self.get_passwd_hash()
        username = input("Username: ")
        password = stdiomask.getpass(prompt="Password: ")
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