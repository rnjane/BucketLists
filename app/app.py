import bucket_lists
import users
from flask import Flask
from flask import render_template, request, redirect, flash, url_for

import forms
from models import bucket_list_item

app = Flask(__name__)

app.config.from_object('config')


USER = users.User()
BUCKETLIST = bucket_lists.BucketLists()
ITEM = bucket_list_item.Items()


@app.route('/')
def home():
    '''index page function'''
    return redirect(url_for('register'))


@app.route('/logout')
def logout():
    USER.logout()
    return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    '''Login function'''
    form = forms.LoginForm(request.form)
    if request.method == 'POST':
        if USER.login_user(form.username.data, form.password.data) == 'Loged in succesfully':
            flash('You were successfully logged in')
            return redirect(url_for('bucketlists'))
        else:
            flash('Invalid username or password. Please try again!')
            return render_template('login.html', form=forms.LoginForm())
    else:
        return render_template('login.html', form=forms.LoginForm())


@app.route('/register', methods=['POST', 'GET'])
def register():
    '''register function'''
    form = forms.SignUpForm(request.form)
    if request.method == 'POST':
        if request.form['password'] != request.form['cpassword']:
            flash('passwords dont match, try again')
            return render_template('register.html', form=form)
        if USER.createUser(request.form['username'], \
                           request.form['password']) == 'succes':
            flash('Account succesfully created')
            return redirect(url_for('login'))
        else:
            flash("Username already in use. Use a different username.")
            return render_template('register.html', form=form)
    elif request.method == 'GET':
        return render_template('register.html', form=form)


@app.route('/bucketlists', methods=['POST', 'GET'])
def bucketlists():
    '''Bucket lists function'''
    form1 = forms.NewBucketList(request.form)
    form = forms.EditBucket(request.form)
    buckets = BUCKETLIST.view_buckets()
    return render_template('bucketlists.html', \
                           blists=buckets, form=form, form1=form1)


@app.route('/bucketlists/addbucket', methods=['POST', 'GET'])
def addbucket():
    '''Add Bucket lists function'''
    if request.method == 'POST':
        if BUCKETLIST.create_bucket(request.form['name']) == 'Bucket already exists. Use a different name':
            flash('Bucket already exists. Use a different name')
            return redirect(url_for('bucketlists'))
        return redirect(url_for('bucketlists'))
    else:
        return redirect(url_for('bucketlists'))


@app.route('/bucketlists/removebucket', methods=['POST', 'GET'])
def removebucket():
    '''Edit Bucket lists function'''
    if request.method == 'POST':
        BUCKETLIST.delete_bucket(request.form['name'])
        flash('Bucket deleted succesfully')
        return redirect(url_for('bucketlists'))
    else:
        return redirect(url_for('bucketlists'))


@app.route('/bucketlists/<b_key>/items', methods=['POST', 'GET'])
def viewitems(b_key):
    '''View items in a bucket list'''
    form1 = forms.NewItem(request.form)
    form = forms.EditItem(request.form)
    if not bucket_lists.currentbucket:
        bucket_lists.currentbucket.append(b_key)
    else:
        bucket_lists.currentbucket[0] = b_key
    items = ITEM.view_items()
    return render_template('tasks.html', items=items, form=form, form1=form1, blist=b_key)


@app.route('/bucketlists/<b_key>/edit', methods=['POST', 'GET'])
def editbucket(b_key):
    '''Edit bucket list name'''
    form = forms.EditItem(request.form)
    return render_template('editbucketlist.html', form=form, blist=b_key)


@app.route('/bucketlists/<b_key>/delete', methods=['POST', 'GET'])
def deletebucket(b_key):
    '''delete bucket list'''
    form = forms.DeleteBucket(request.form)
    return render_template('deletebucket.html', form=form, blist=b_key)


@app.route('/bucketlist/delete', methods=['POST', 'GET'])
def deletebuket():
    '''delete bucket'''
    form = forms.DeleteBucket(request.form)
    if request.method == 'POST':
        BUCKETLIST.delete_bucket(request.form['name'])
        return redirect(url_for('bucketlists'))
    else:
        return redirect(url_for('bucketlists'))


@app.route('/items/additem', methods=['POST', 'GET'])
def additem():
    '''Add item function'''
    if request.method == 'POST':
        nme = request.form['name']
        blist = request.form['bucketlist']
        if ITEM.create_item(nme) == 'Item already exists. Use a different name':
            flash('Item already exists. Use a different name')
            return redirect(url_for('viewitems', b_key=blist))
        return redirect(url_for('viewitems', b_key=blist))
    else:
        return redirect(url_for('viewitems'))


@app.route('/bucketlist/edit', methods=['POST', 'GET'])
def editbuket():
    '''edit bucket'''
    form = forms.EditBucket(request.form)
    if request.method == 'POST':
        BUCKETLIST.edit_bucket(request.form['name'], \
                               request.form['newname'])
        return redirect(url_for('bucketlists'))
    else:
        return redirect(url_for('bucketlists'))


@app.route('/items/edititem', methods=['POST', 'GET'])
def edititem():
    '''Edit item function'''
    if request.method == 'POST':
        blist = bucket_lists.currentbucket[0]
        ITEM.edit_item(request.form['name'], request.form['newname'])
        return redirect(url_for('viewitems', b_key=blist))
    else:
        return redirect(url_for('viewitems'))


@app.route('/items/removeitem', methods=['POST', 'GET'])
def removeitem():
    '''Remove item function'''
    if request.method == 'POST':
        blist = bucket_lists.currentbucket[0]
        ITEM.delete_item(request.form['name'])
        return redirect(url_for('viewitems', b_key=blist))
    else:
        return redirect(url_for('viewitems'))

if __name__ == '__main__':
    app.run(debug=True)
