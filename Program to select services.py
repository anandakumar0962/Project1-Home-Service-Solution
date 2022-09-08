
users_data = [{"user_name" : "Anandkumar", "mobile_number" : "9876543210",  "password" : "anand0962"},
                  {"user_name" : "Hariharan", "mobile_number" : "9876543201", "password" : "hari1302"}]


service_list = [ { "location" : "chennai", "services" : ["home clean", "plumber", "electrician", "carpenter", "pest control", "appliance repair", "painter"]},
                 { "location" : "thiruvallur", "services" : ["home clean", "plumber", "electrician", "painter"]},
                 { "location" : "porur", "services" : ["home clean", "plumber", "electrician", "carpenter", "painter"]},
                 { "location" : "tambaram", "services" : ["home clean", "plumber", "electrician", "appliance repair", "painter"]},
                 { "location" : "adyar", "services" : ["home clean", "plumber", "electrician", "carpenter", "appliance repair", "painter"]}]
class Signup:

    def __init__(self, user_name, mobile_number, password):
        self.user_name = user_name
        self.mobile_number = mobile_number
        self.password = password

       
    def signup_user(self):

        user_name = [self.user_name]
        mobile_number = [self.mobile_number]

        user_check = [d for d in users_data if d["user_name"] in user_name or d["mobile_number"] in mobile_number]

        if user_check != []:
            print("Username or Mobile number already exist")

        else:
            new_user = {"user_name" : self.user_name, "mobile_number" : self.mobile_number, "password": self.password}
            users_data.append(new_user)
            print(users_data)

            
class Login:

    def __init__(self, mobile_number, password):
        self.mobile_number = mobile_number
        self.password = password

    def login_user(self):
        mobile_number = [self.mobile_number]
        password = [self.password]
        
        login = [d for d in users_data if d["mobile_number"] in mobile_number and d["password"] in password]
        
        
        if login != []:
            print("Login Successfully")
            
        else:
            print("Email Id or Password is invalid")
    
class Services:

    def __init__(self, user_name, mobile_number):
        self.user_name = user_name
        self.mobile_number = mobile_number
        

    def service(self):
    
    
        cust_loc = [input("Enter the location\n")]
        check_loc = [d for d in service_list if d["location"] in cust_loc]
        if check_loc !=[]:

            for i in check_loc:
                show_service = i.get("services")
                for j in show_service:
                    print(j)
                print("\n")
                get_service = input("Enter the service\n")
                cnfrm_service = list(get_service.split("-"))
                set1 = set(cnfrm_service)
                set2 = set(show_service)

                if set1.intersection(set2):
                    service_details = f"Customer Name: {self.user_name}\nPhone Number: {self.mobile_number}"
                    print(service_details)
                    print("Service List:\n",','.join(cnfrm_service))
                    
                else:

                    print("Invalid input")

      
choice = input("Enter \'signup\' or \'login\'\n\n")
if choice == "signup":
    
     user_name = input("Enter Username which contains atleast 8 characters\n\n")
     if len(user_name) < 8:
         print("The name you entered is too small")

     else:
         mobile_number = input("Enter Mobile number\n")
         password = input("Enter Password\n")
         cnfrm_password = input("Confirm password\n")
         if password == cnfrm_password:
             signupdata = Signup(user_name, mobile_number, password)
             Signup.signup_user(signupdata)
             service_data = Services(user_name, mobile_number)
             Services.service(service_data)
         else:
             print("Ensure password and confirm password")

     
elif choice == "login":
    user_name = input("Enter the Username\n") 
    mobile_number = input("Enter the Mobile Number\n")
    password = input("Enter the Password\n")
    logindata = Login(mobile_number, password)
    Login.login_user(logindata)
    service_data = Services(user_name, mobile_number)
    Services.service(service_data)

else:
    print("Invalid Input")
