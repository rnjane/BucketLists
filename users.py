
users = {}
currentuser = []


class User():
    '''This class defines actions related to the users of the app'''
    __username = ''
    __password = ''

    def createUser(self, username, password):
        '''Method to register users'''
        if type(username) is list or type(username) is dict:
            return 'wrong data format'
        if users.get(username):
            return 'Username already exists. Use a different one'
        else:
            users[username] = password
        return 'succes'

    def login_user(self, username, password):
        '''Method to log users in'''
        if len(users) < 1:
            return 'No users registered. Create an account first'
        else:
            if users.get(username):
                if users[username] == password:
                    if not currentuser:
                        currentuser.append(username)
                    else:
                        currentuser[0] = 'username'
                    return 'Loged in succesfully'
                else:
                    return 'Wrong Password'
            else:
                return 'User does not exist'

    def logout(self):
        '''log out method'''
        currentuser[:] = []
