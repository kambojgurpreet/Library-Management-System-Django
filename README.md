# Library-Management-System-Django
Library Management System APIs implemented using DRF

### API Endpoints

#### GET

* **/author/** (All Authors Information endpoint)
* **/author/<int: pk>** (Author Information with id = pk endpoint)
* **/book/** (All Books Information endpoint)
**/book/<int: pk>** (Book Information with id = pk endpoint)
* **/customer/** (All Customer Information endpoint)
**/customer/<int: pk>** (Customer Information with id = pk endpoint)

#### POST

* **/book/** (Insert Book Information endpoint)

#### PUT

* **/book/<int: pk>** (Update Book Information with id = pk endpoint)

#### DELETE

* **/book/<int: pk>** (DELETE Book Information with id = pk endpoint)

### Install 

    pip install -r requirements.txt

#### Note
* **Create library/logs/debug.log**
* **Add library/library/config.json**

### Usage
    
    cd library
    python manage.py makemigrations
    python manage.py migrate
    python manage.py makemigrations api
    python manage.py migrate api
    python manage.py runserver
