
users = {}
currentuser = []

curruser = currentuser
buckets = {}
currentbucket = []
curritem = currentbucket
items = {}


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


class BucketLists():
    '''Class definition for the bucketlists classs'''
    __name = ''
    __username = ''

    def create_bucket(self, bucketname):
        '''add a bucket method'''
        if curruser[0] not in buckets:
            buckets[curruser[0]] = []
        if bucketname in buckets.get((curruser[0])):
            return 'Bucket already exists. Use a different name'
        buckets[curruser[0]].append(bucketname)
        return 'succes'

    def current_bucket(self, name):
        '''add current bucket method'''
        currentbucket.append(name)

    def view_buckets(self):
        '''view all buckets method'''
        if bool(buckets):
            if buckets.get(curruser[0]):
                return buckets.get(curruser[0])
            return []
        return []

    def delete_bucket(self, bucketname):
        '''delete a bucket method'''
        if bucketname in buckets.get(curruser[0]):
            buckets[curruser[0]].remove(bucketname)
        return buckets

    def edit_bucket(self, oldname, newname):
        '''edit a bucket method'''
        if oldname in buckets.get(curruser[0]):
            buckets[curruser[0]].remove(oldname)
            buckets[curruser[0]].append(newname)
        return buckets


class Items():
    __itemname = ''
    __itemlist = ''

    def create_item(self, itemname):
        '''create item method'''
        if curritem[0] not in items:
            items[curritem[0]] = []
        if itemname in items.get((curritem[0])):
            return 'Item already exists. Use a different name'
        items[curritem[0]].append(itemname)

    def view_items(self):
        '''view all items method'''
        if bool(items):
            if items.get(curritem[0]):
                return items.get(curritem[0])
            return []
        return []

    def delete_item(self, itemname):
        '''delete an item method'''
        if itemname in items.get(curritem[0]):
            items[curritem[0]].remove(itemname)
        return items

    def edit_item(self, oldname, newname):
        '''edit item method'''
        if oldname in items.get(curritem[0]):
            items[curritem[0]].remove(oldname)
            items[curritem[0]].append(newname)
        return items