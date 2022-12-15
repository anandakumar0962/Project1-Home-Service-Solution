class Login:
    users_data = [{"user_id" : "anand0962@gmail.com", "password" : "anand0962"}, {"user_id" : "hari1302@gmail.com", "password" : "hari1302"}]
    
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
       
    def login(self):
        email_id = [self.user_id]
        password = [self.password]
        login = [d for d in self.users_data if d["user_id"] in email_id and d["password"] in password]
        if login != []:
            print("Login Successfully")
            
        else:
            print("Email Id or Password is invalid")
        
def main():
            
    print("Welcome to Home Service Solution")
    choice = input("Enter login or signup\n")
    if choice == "login":
        email_id = input("Enter the Mail Id\n")
        password = input("Enter the password\n")
            
        login_data = Login(email_id, password)
        Login.login(login_data)
        
main()