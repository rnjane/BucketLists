

import unittest
import bucket_lists, bucket_list_item, users


class BucketListTest(unittest.TestCase):
    '''Tests for the Bucket List Class'''
    def test_add_bucket_list_works(self):
        '''Tests if add functionality works'''
        user = users.User()
        user.createUser('peter', 1234)
        user.login_user('peter', 1234)
        bucket_list = bucket_lists.BucketLists()
        bucket_list.create_bucket('Hike')
        if 'Hike' in bucket_lists.buckets.get(users.currentuser[0]):
            checkitem = True
        self.assertEqual(checkitem, True)

    def test_no_duplicate_bucket_lists(self):
        '''Test to check if duplicate bucket list can be added'''
        bucket_list = bucket_lists.BucketLists()
        bucket_list.create_bucket('Hike')
        bucket_list.create_bucket('Hike')
        checkexists = False
        if len(list(set(bucket_lists.buckets.keys()))) \
            == len(bucket_lists.buckets.keys()):
            checkexists = True
        self.assertEqual(checkexists, True)

    def test_delete_bucket_list_item(self):
        '''Tests if delete functionality works'''
        bucket_list = bucket_lists.BucketLists()
        bucket_list.create_bucket('Camp')
        bucket_list.delete_bucket('Camp')
        delete_not_working = False
        if 'Camp' in bucket_lists.buckets.get(users.currentuser[0]):
            delete_not_working = True
        self.assertEqual(delete_not_working, False)

    def test_edit_bucket_list_item(self):
        '''Tests if edit functionality works'''
        bucket_list = bucket_lists.BucketLists()
        bucket_list.create_bucket('Camp')
        bucket_list.edit_bucket('Camp', 'Scouting')
        edit_not_working = False
        if 'Camp' in bucket_lists.buckets.get(users.currentuser[0]):
            edit_not_working = True
        self.assertEqual(edit_not_working, False)


class BucketListItemTest(unittest.TestCase):
    '''Tests for the Bucket List Items Class'''

    def test_add_bucket_list_item_works(self):
        '''Tests if add functionality works'''
        bkt = bucket_lists.BucketLists()
        bkt.current_bucket('bucket1')
        item = bucket_list_item.Items()
        item.create_item('raft')
        add_item_works = False
        if 'raft' in bucket_list_item.items.get(bucket_lists.currentbucket[0]):
            add_item_works = True
        self.assertEqual(add_item_works, True)

    def test_no_duplicate_list_item(self):
        '''Test to check if duplicate list item can be added'''
        item = bucket_list_item.Items()
        item.create_item('swim')
        item.create_item('swim')
        duplicate_exists = True
        if len(list(set(bucket_list_item.items.keys())))\
                == len(bucket_list_item.items.keys()):
            duplicate_exists = False
        self.assertEqual(duplicate_exists, False)

    def test_delete_item(self):
        '''Tests if delete functionality works'''
        item = bucket_list_item.Items()
        item.create_item('do assignment')
        item.delete_item('do assignment')
        delete_not_working = False
        if 'do assignment' in bucket_list_item.items.get(bucket_lists.currentbucket[0]):
            delete_not_working = True
        self.assertEqual(delete_not_working, False)

    def test_edit_item(self):
        '''Tests if edit functionality works'''
        item = bucket_list_item.Items()
        item.create_item('task')
        item.edit_item('task', 'task1')
        edit_not_working = False
        if 'task' in bucket_list_item.items.get(bucket_lists.currentbucket[0]):
            edit_not_working = True
        self.assertEqual(edit_not_working, False)
