import bucket_lists

curritem = bucket_lists.currentbucket
items = {}
item_status = {}


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
