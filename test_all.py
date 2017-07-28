
from app import models
import unittest
import app

class ViewTest(unittest.TestCase):
    '''Basic app tests'''
    def setUp(self):
        self.app = app.app.test_client()

    def test_indexpage_succesful(self):
        '''Test home page route'''
        response = self.app.get('/', follow_redirects=True)
        print(response.data)
        self.assertEqual(response.status_code, 200)

class BucketListTest(unittest.TestCase):
    '''Tests for the Bucket List Class'''
    def test_addbucketlist_succesful(self):
        '''Tests if add functionality works'''
        user = models.User()
        user.createUser('peter', 1234)
        user.login_user('peter', 1234)
        bucket_list = models.BucketLists()
        bucket_list.create_bucket('Hike')
        if 'Hike' in models.buckets.get(models.currentuser[0]):
            checkitem = True
        self.assertEqual(checkitem, True)

    def test_bucketlists_duplicatebucketlists(self):
        '''Test to check if duplicate bucket list can be added'''
        bucket_list = models.BucketLists()
        bucket_list.create_bucket('Hike')
        bucket_list.create_bucket('Hike')
        checkexists = False
        if len(list(set(models.buckets.keys()))) \
            == len(models.buckets.keys()):
            checkexists = True
        self.assertEqual(checkexists, True)

    def test_deletebucketlist_sucessful(self):
        '''Tests if delete functionality works'''
        bucket_list = models.BucketLists()
        bucket_list.create_bucket('Camp')
        bucket_list.delete_bucket('Camp')
        delete_not_working = False
        if 'Camp' in models.buckets.get(models.currentuser[0]):
            delete_not_working = True
        self.assertEqual(delete_not_working, False)

    def test_editbucketlist_succesful(self):
        '''Tests if edit functionality works'''
        bucket_list = models.BucketLists()
        bucket_list.create_bucket('Camp')
        bucket_list.edit_bucket('Camp', 'Scouting')
        edit_not_working = False
        if 'Camp' in models.buckets.get(models.currentuser[0]):
            edit_not_working = True
        self.assertEqual(edit_not_working, False)


class BucketListItemTest(unittest.TestCase):
    '''Tests for the Bucket List Items Class'''

    def test_additem_succesful(self):
        '''Tests if add functionality works'''
        bkt = models.BucketLists()
        bkt.current_bucket('bucket1')
        item = models.Items()
        item.create_item('raft')
        add_item_works = False
        if 'raft' in models.items.get(models.currentbucket[0]):
            add_item_works = True
        self.assertEqual(add_item_works, True)

    def test_items_duplicateitems(self):
        '''Test to check if duplicate list item can be added'''
        item = models.Items()
        item.create_item('swim')
        item.create_item('swim')
        duplicate_exists = True
        if len(list(set(models.items.keys())))\
                == len(models.items.keys()):
            duplicate_exists = False
        self.assertEqual(duplicate_exists, False)

    def test_deleteitem_succesful(self):
        '''Tests if delete functionality works'''
        item = models.Items()
        item.create_item('do assignment')
        item.delete_item('do assignment')
        delete_not_working = False
        if 'do assignment' in \
                            models.items.get(models.currentbucket[0]):
            delete_not_working = True
        self.assertEqual(delete_not_working, False)

    def test_edititem_succesful(self):
        '''Tests if edit functionality works'''
        item = models.Items()
        item.create_item('task')
        item.edit_item('task', 'task1')
        edit_not_working = False
        if 'task' in models.items.get(models.currentbucket[0]):
            edit_not_working = True
        self.assertEqual(edit_not_working, False)


class UserTest(unittest.TestCase):
    '''Tests for user functionalities'''
    def test_register_succesful(self):
        '''Tests if register functionality works'''
        user = models.User()
        user.createUser('peter', 'password')
        if 'peter' in models.users:
            checkuser = True
        self.assertEqual(checkuser, True)

    def test_register_duplicateusers(self):
        '''Test to check if duplicate username can be added'''
        user = models.User()
        user.createUser('ken', 'pass')
        user.createUser('ken', '1234')
        if len(list(set(models.users.keys()))) == len(models.users.keys()):
            checkexists = True
        self.assertEqual(checkexists, True)

    def test_login_wrongcredentials(self):
        '''Test user exists before login'''
        user = models.User()
        unameexists = False
        if user.login_user('ptr', 'pass') == 'User does not exist':
            unameexists = True
        self.assertEqual(unameexists, True)

    def test_register_wrongcredentials(self):
        '''check if wrong password is entered'''
        user = models.User()
        check = user.createUser([], 'jj')
        self.assertEqual(check, 'wrong data format')
