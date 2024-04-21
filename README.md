# Get gender by name API (Мужчина - male or Женщина - female)
* Available at [genderbyname.sytes.net](https://genderbyname.sytes.net/api/get_gender_by_name/)
* [API documentation](https://genderbyname.sytes.net/api/schema/redoc/).
* Source code is available on [public repository](https://github.com/beluza-n/gender_by_name)

Authors:
* Anastasia Grechkina (Github beluza-n, telegram @beluza_n)

## Description
Created as test case for Python-developer job at [анверали.рф](https://анверали.рф/). Uses Django Rest Framework. Uses PostgreSQL as database.
Recieves id and name. Checks if name is in names_man and names_woman tables. Response with gender if found.

## Stack:
* Python
* Django Rest Framework
* PostgreSQL


## API request examples

Example 1. Request to the server:
```json
{
"id": 1,
"name": "Виктор"
}
```

Server response:
```json
{
"id": 1,
"name": "Виктор",
"gender": "Мужчина"
}
```

Example 2. Request to the server:
```json
{
"id": 1,
"name": "Анастасия"
}
```

Server response:
```json
{
"id": 1,
"name": "Анастасия",
"gender": "Женщина"
}
```

### How to run the project:
Clone repository and go to it with the terminal::

```
git clone git@github.com:beluza-n/gender_by_name.git
```
```
cd gender_by_name
```

Create and activate virtual environment:

```
python -m venv venv
(python3 in ubuntu)
```
```
source venv/Scripts/activate
(source venv/bin/activate in ubuntu)
```

Update pip (optional):

```
python -m pip install --upgrade pip
```

Install dependencies from the requirements.txt:

```
pip install -r requirements.txt
```

Run migrations:

```
python manage.py migrate
```

Connect to your PostgreSQL database "names":
```
psql -h localhost names postgres
```

Fill tables with male and female russian names (change path according to your project folder):

```
\COPY names_man FROM '/home/user/gender_by_name/data/male_names.csv' DELIMITER ',' CSV HEADER;
\COPY names_woman FROM '/home/user/gender_by_name/data/female_names.csv' DELIMITER ',' CSV HEADER;
```

Launch the Django project:
```
python manage.py runserver
```
