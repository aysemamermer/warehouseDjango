# warehouseDjango

# Equipment Management API

This Django REST framework (DRF) project provides API endpoints for managing machines and equipment associated with those machines.

## Installation

Install Project:
```
git clone https://github.com/aysemamermer/warehouseDjango.git
```

Project Folder:
```
cd warehouseDjango
```
The Python packages required for the project are as follows:

`Django==5.0`

`djangorestframework==3.14.0`

You can install dependencies by going to the project folder and running the following command:
```
pip install -r requirements.txt
```

Create user:
```
python manage.py createsuperuser
```

Run:
```
python manage.py runserver
```

## Database

```
python manage.py migrate
```

## Equipment API Endpoints

### List and Create Equipment

- **Endpoint:** `/api/equipment/`
- **Methods:** GET, POST
- **Description:** 
  - GET: Retrieve a list of all equipment.
  - POST: Create a new equipment entry.
- **Parameters:** None for GET, Equipment details for POST
- **Response:** JSON representation of equipment list or newly created equipment.

### Retrieve, Update, and Delete Equipment

- **Endpoint:** `/api/equipment/<int:pk>/`
- **Methods:** GET, PUT, DELETE
- **Description:** 
  - GET: Retrieve details of a specific equipment.
  - PUT: Update details of a specific equipment.
  - DELETE: Delete a specific equipment.
- **Parameters:** Equipment ID (pk) for GET, PUT, and DELETE
- **Response:** JSON representation of equipment details or success message for DELETE.


## Machine API Endpoints

### List and Create Machines

- **Endpoint:** `/api/machines/`
- **Methods:** GET, POST
- **Description:** 
  - GET: Retrieve a list of all machines.
  - POST: Create a new machine entry.
- **Parameters:** None for GET, Machine details for POST
- **Response:** JSON representation of machine list or newly created machine.

### Retrieve, Update, and Delete Machines

- **Endpoint:** `/api/machines/<int:pk>/`
- **Methods:** GET, PUT, DELETE
- **Description:** 
  - GET: Retrieve details of a specific machine.
  - PUT: Update details of a specific machine.
  - DELETE: Delete a specific machine.
- **Parameters:** Machine ID (pk) for GET, PUT, and DELETE
- **Response:** JSON representation of machine details or success message for DELETE.



## IMPORTANT
You must add your origin to settings.py file 

```
CORS_ALLOWED_ORIGINS = ["http://localhost:8080","http://your.origin"]
```
