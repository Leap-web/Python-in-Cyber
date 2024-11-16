print("Thay_Bunleap G2")
print("I. Encapsulation")
print("Exercise 1")
class User:
    def __init__ (self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return 'Username: {}'.format(self.__username)

    def verify_password(self):
        if self.__password == 1234:
            return 'Password Verified: {}'.format(True)
        else:
            return 'Password Verified: {}'.format(False)

user = User("cyber_user", 1234)
user1 = User("cyber_user", 1233)
print(user.get_username())
print(user.verify_password())
print(user1.verify_password())

print("\nExercise 2")
class UserProfile:
    def __init__(self, username, phone_number):
        self.__username = username
        self.__phone_number = phone_number

    def verify_password(self, phone_number):
        self.__phone_number = phone_number

    def display_info(self):
        return 'Username: {}, Phone Number: XXX-XXX-{}'.format(self.__username, self.__phone_number[-4:])

    def update_phone_number(self, old_phone_number, new_phone_number):
        if self.__phone_number == old_phone_number:
            self.__phone_number = new_phone_number
            print("Contact info updated successfully.")
        else:
            print('Phone number not exist.')

user_profile = UserProfile("cyber_user", "123-456-7890")
print(user_profile.display_info())
user_profile.update_phone_number("123-456-7890", "123-456-4321")
print(user_profile.display_info())

print("\nII. Inheritance")
print("Exercise 3")
class Malware:
    def __init__(self, describe):
        self.describe = describe

    def describe(self):
        print(f"{self.describe}: This is a malware.")

class Ransomware(Malware):
    def encrypt_files(self):
        print(f"{self.describe}: Files are being encrypted.")

malware = Malware("Malware Description")
ransomware = Malware("Ransomware Description")
ransomwares = Ransomware("Ransomware Action")
Malware.describe(malware)
Ransomware.describe(ransomware)
Ransomware.encrypt_files(ransomwares)

print("\nExercise 4")
class Virus(Malware):
    def replicate(self):
        print(f"{self.describe}: Virus is replicating.")

class Trojan(Malware):
    def hide_in_files(self):
        print(f"{self.describe}: Hiding in files.")

class KeyLogger(Trojan):
    def __init__(self, describe):
        self.describe = describe

    def describe(self):
        print(f"{self.describe}: This is a keylogger. Capturing keystrokes.")

viruss = Malware("Virus Description")
virus = Virus("Virus Action")
trojans = Malware("Trojan Description")
trojan = Trojan("Trojan Action")
keyloggers = KeyLogger("KeyLogger Description")
keylogger = Trojan("Keylogger Action")
Virus.describe(viruss)
Virus.replicate(virus)
Trojan.describe(trojans)
Trojan.hide_in_files(trojan)
KeyLogger.describe(keyloggers)
KeyLogger.hide_in_files(keylogger)

print("\nIII. Polymorphism")
print("Exercise 5")
class Logger:
    def log(self, message = None, error_code = None, details = None):
        if message is not None:
            print(f"Log: {message}")
        elif error_code is not None and details is not None:
            print(f"Error Code: {error_code}, Details: {details}")
        else:
            print("Unknown log format")

logger = Logger()
logger.log("System started")
logger.log(error_code=404, details={'url': '/not-found'})
logger.log()

print("\nExercise 6")
class FirewallRule:
    def __init__ (self, rule):
        self.rule = rule

    def apply_rule(self):
        print(f"{self.rule}: Applying generic rule.")

class IPBlockRule(FirewallRule):
    def apply_rule(self):
        print(f"{self.rule}: Blocking IP address.")

class PortBlockRule(FirewallRule):
    def apply_rule(self):
        print(f"{self.rule}: Blocking port number.")

firewall = [FirewallRule("Firewall Action"), IPBlockRule("Firewall Action"), PortBlockRule("Firewall Action")]
for rule in firewall:
    rule.apply_rule()