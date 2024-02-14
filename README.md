# Relationships in FastAPI
## Features:
* Many to one relationship (ForeignKey)
* Many to many relationships 
* One to one relationship

## Many to one relationship (ForeignKey)
Instances
* Parents
* Child
Parents have many childs but childs have many parents

### API list for M-1 relationships
| SRL | METHOD | ROUTE | FUNCTIONALITY | Required Fields | 
| ------- | ------- | ----- | ------------- | ------------- |
| *1* | *POST* | ```/login``` | _Login user_| _email, password_|
| *2* | *POST* | ```/users/``` | _Create new user_|_email, password_|
| *3* | *GET* | ```/users/``` | _Get all users list_|_None_|
| *4* | *GET* | ```/users/me/``` | _Get current user details_|_None_|

# Setup
The first thing to do is to clone the repository:
```sh
$ https://github.com/MahmudJewel/fastapi-starter-kit
```

Create a virtual environment to install dependencies in and activate it:
```sh
$ cd fastapi-starter-kit
$ python -m venv venv
$ source venv/bin/activate
```
Then install the dependencies:
```sh
# for fixed version
(venv)$ pip install -r requirements.txt

# or for updated version
(venv)$ pip install -r dev.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
# db migrations
(venv)$ alembic upgrade head

# start the server 
(venv)$ uvicorn app.main:app --reload
```

## User module's API
| SRL | METHOD | ROUTE | FUNCTIONALITY | Required Fields | 
| ------- | ------- | ----- | ------------- | ------------- |
| *1* | *POST* | ```/login``` | _Login user_| _email, password_|
| *2* | *POST* | ```/users/``` | _Create new user_|_email, password_|
| *3* | *GET* | ```/users/``` | _Get all users list_|_None_|
| *4* | *GET* | ```/users/me/``` | _Get current user details_|_None_|
| *5* | *GET* | ```/users/{user_id}``` | _Get indivisual users details_|_None_|
| *6* | *PATCH* | ```/users/{user_id}``` | _Update the user partially_|_email, password, is_active, role_|
| *7* | *DELETE* | ```/users/{user_id}``` | _Delete the user_|_None_| _admin_|
| *8* | *GET* | ```/``` | _Home page_|_None_|
| *9* | *GET* | ```/admin``` | _Admin Dashboard_|_None_|


# Tools
### Back-end
#### Language:
	Python

#### Frameworks:
	FastAPI
    pydantic
	
#### Other libraries / tools:
	SQLAlchemy
    starlette
    uvicorn
    python-jose
    alembic

# Happy Coding
## From ==> Mahmud

