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


class Signup(Login):
    
    
    def __init__(self, user_id, password, cnfrm_password):
        super().__init__(user_id, password)
        self.cnfrm_password = cnfrm_password
        
    def signup(self):
        
        if self.password == self.cnfrm_password:
            email_id = [self.user_id]
            password = [self.password]
            
            signup = [d for d in self.users_data if d["user_id"] in email_id]
            
            if signup != []:
                print("Email Id already exist")
            else:
                
                new_user = {"user_id" : self.user_id, "password" : self.password}
                self.users_data.append(new_user)
                print("Signup Successfully")
                print(self.users_data)
                
        else:
            print("Passwords are mismatch")
            
            
def main():
            
    print("Welcome to Home Service Solution")
    choice = input("Enter login or signup\n")
    if choice == "login":
        user_id = input("Enter the Email Id\n")
        password = input("Enter the password\n")
            
        login_data = Login(user_id, password)
        Login.login(login_data)
            
    elif choice == "signup":
        user_id = input("Enter a Email Id\n")
        password = input("Enter  password\n")
        cnfrm_password = input("Confrim Password\n")
            
        signup_data = Signup(user_id, password, cnfrm_password)
        Signup.signup(signup_data)
    else:
        print("Invalid Input")
        
main()
