'''

'''
from wtforms import BooleanField, \
 StringField, PasswordField, validators, SubmitField, Form, HiddenField


class LoginForm(Form):
    '''Login Form'''
    username = StringField('User Name', [validators.DataRequired()])
    password = PasswordField('Password', \
                             [validators.DataRequired\
                              (message='Password required')])
    submit = SubmitField('Submit')


class SignUpForm(Form):
    '''Signup Form'''
    username = StringField('Username', [validators.Length(min=2, max=25)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    submit = PasswordField('Repeat Password')


class NewBucketList(Form):
    '''New Bucket List Form'''
    name = StringField('Tags', [validators.Length(min=1, max=20)])


class NewItem(Form):
    '''New Bucket List Form'''
    name = StringField('Tags', [validators.Length(min=1, max=20)])
    bucketlist = StringField('bucketlist', [validators.Length(min=1, max=20)])


class EditItem(Form):
    '''Edit Form'''
    name = StringField('Tags', [validators.Length(min=1, max=20)])
    newname = StringField('Tags', [validators.Length(min=1, max=20)])


class EditBucket(Form):
    '''Edit Form'''
    name = StringField('Tags', [validators.Length(min=1, max=20)])
    newname = StringField('Tags', [validators.Length(min=1, max=20)])


class DeleteBucket(Form):
    '''Delete Form'''
    name = StringField('Tags', [validators.Length(min=1, max=20)])
