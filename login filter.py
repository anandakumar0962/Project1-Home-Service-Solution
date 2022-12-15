# Method using filter function 

print('Welcome to Home Serive Application')


class users:
    users_list = [
        {'name': 'Sanjay', 'email': 'sanjay@gmail.com', 'password': 'sanjay'},
        {'name': 'raj', 'email': 'raj@gmail.com', 'password': 'raj'}
    ]

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class check_login(users):
    def sign_up(self):
        single_user = {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

        check_list = list(
            filter(lambda x: x['email'] == self.email and x['password'] == self.password, check_login.users_list))

        if check_list == []:
            check_login.users_list.append(single_user)
            return "You added as a user"

        elif check_list[0]['email'] == self.email:
            return "User already exist"


def main():
    name = input("Enter your name:")
    email = input("Enter your email ID:")
    password = input("Enter your password:")
    user1 = check_login(name, email, password)
    print(user1.sign_up())


if __name__ == '__main__':
    main()
