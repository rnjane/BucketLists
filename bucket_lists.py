import users

curruser = users.currentuser
buckets = {}
currentbucket = []


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

