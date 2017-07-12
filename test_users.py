import unittest

import users


class UserTest(unittest.TestCase):
    '''Tests for user functionalities'''
    def test_register_works(self):
        '''Tests if register functionality works'''
        user = users.User()
        user.createUser('peter', 'password')
        if 'peter' in users.users:
            checkuser = True
        self.assertEqual(checkuser, True)

    def test_no_duplicate_user(self):
        '''Test to check if duplicate username can be added'''
        user = users.User()
        user.createUser('ken', 'pass')
        user.createUser('ken', '1234')
        if len(list(set(users.users.keys()))) == len(users.users.keys()):
            checkexists = True
        self.assertEqual(checkexists, True)

    def test_user_exists(self):
        '''Test user exists before login'''
        user = users.User()
        unameexists = False
        if user.login_user('ptr', 'pass') == 'User does not exist':
            unameexists = True
        self.assertEqual(unameexists, True)

    def test_wrong_password_format(self):
        '''check if wrong password is entered'''
        user = users.User()
        check = user.createUser([], 'jj')
        self.assertEqual(check, 'wrong data format')
