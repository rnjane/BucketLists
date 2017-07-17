[![Build Status](https://travis-ci.org/rnjane/BucketLists.svg?branch=master)](https://travis-ci.org/rnjane/BucketLists)
[![Coverage Status](https://coveralls.io/repos/github/rnjane/BucketLists/badge.svg?branch=develop)](https://coveralls.io/github/rnjane/BucketLists?branch=develop)
# Introduction

* **Bucket Lists App** is a Flask Powered Bucket Lists App. Bucket List app helps users record things they want to achieve or experience before reaching a certain age.
* Click [here](https://bucket-lists-app.herokuapp.com/register) to see a working version.
# Features
  * User should be able to signup and login
  * User should be able to make a Bucket List.
  * User should be able to add tasks to a bucketlist.
  * User should be able to edit and delete bucketlists.
  * User should be able to edit and delete bucketlists items.
  
# Dependencies

# Back End Dependencies
* This app functionality depends on multiple python packages including;
  * Flask==0.11.1
  * Flask-PageDown==0.2.2
  * Flask-WTF==0.13.1
  * Jinja2==2.8
  * MarkupSafe==0.23
  * WTForms==2.1
  * Werkzeug==0.11.11
  * click==6.6
  * gunicorn==19.6.0
  * itsdangerous==0.24
  * passlib==1.6.5

# Installation
To run this project, you'll need a working installation of python 3 and pip. Flask should also be installed.

## To install the app:
1. Clone this repository - https://github.com/rnjane/BucketLists
2. Install requirements - pip install requirements.txt
3. Run app.py file.

# Testing
1. Install pytest extension - pip install pytest
2. Run test_all.py with pytest.
- All tests should be passing.

# How to use the application.
1. Create an account, only username and password are needed.
2. Login to your account.
3. Add bucktlist(s).
4. Click edit or delete to edit or delete the respective bucketlist.
5. Click on a bucketlist name to add items to it.
6. Click edit or delete to edit or delete the respective item.
7. To go back to all your bucket lists, click on the application title in the top right.
8. To log out, click on the link labelled logout in the top left corner.



