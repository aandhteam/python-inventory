# Inventory Management System

An Inventory Management System (IMS) developed in Python Django.
## Table of Contents

1. Prerequisites
2. Installation
3. Setup Environment
4. Running the Project
5. Testing

## Prerequisites

To run this project, you need:

- **Python** (version 3.x recommended)
- **pip** (Python package installer)

You can check if you have Python installed by running:

```
bash
python --version
```

If you need to install Python, download it from the official Python website.

### Installation
 - Clone the project repository to your local machine:
 ```
git clone https://github.com/aandhteam/python-inventory.git
cd python-inventory
```

### Create a Virtual Environment

It’s recommended to use a virtual environment for dependencies:

```
python -m venv venv
```

### Activate the Virtual Environment

 - On Windows:
 ``` 
 .\venv\Scripts\activate
```

 - On macOS/Linux:
 ```
source venv/bin/activate
```

### Install Dependencies
 - Install all required Python packages using the requirements.txt file:
 ```
pip install -r requirements.txt
```


### Install Other Dependencies
 ```
pip install djangorestframework
```

### Running the Project
Run the main script to start the project:
 ```
python manage.py runserver
```


### Testing
To run tests, use:
 ```
python manage.py test
```

### URLS
  - Admin: http://localhost:8000/admin
    - Username: admin
    - Password: admin
  - Front-End: http://localhost:8000
