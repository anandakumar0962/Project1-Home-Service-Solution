users_data = [{"username" : "anand", "password" : "123"}, {"username" : "hari", "password" : "234"}]
inputid = ["anand"]
inputpass = ["234"]
login = [d for d in users_data if d["username"] in inputid and d["password"] in inputpass]
print(login)