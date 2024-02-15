# Relationships in FastAPI
## Features:
* Many to one relationship (ForeignKey)
* Many to many relationships 
* One to one relationship

## Many to one relationship (ForeignKey)
Instances
* Parents
* Child

Parents have many childs but childs have one parents

### API list for M-1 relationships
| SRL | METHOD | ROUTE | FUNCTIONALITY | Fields | 
| ------- | ------- | ----- | ------------- | ------------- |
| *1* | *POST* | ```/relation/parents``` | _create parents_| _**name**_|
| *2* | *GET* | ```/relation/parents``` | _All parents info with childs_|_id, name, children(id,name)_|
| *3* | *POST* | ```/relation/child``` | _Create Child_|_**name**, parent_id_|
| *4* | *GET* | ```/relation/child``` | _All child info with parent_id_|_None_|
| *5* | *GET* | ```/relation/child-with-parents-info``` | _All child info with parent info_|_id, name, parent(id, name)_|

#### Example
GET ==> /relation/child-with-parents-info
```sh
[
  {
    "id": 1,
    "name": "Habib",
    "parent": [
      {
        "id": 2,
        "name": "Sattar Miah"
      }
    ]
  },
  {
    "id": 2,
    "name": "Jasim",
    "parent": [
      {
        "id": 1,
        "name": "Abdus Salam"
      }
    ]
  }
]
```


# Setup
The first thing to do is to clone the repository:
```sh
$ https://github.com/MahmudJewel/fastapi-relationship
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

## Happy Coding
From ==> Mahmud

