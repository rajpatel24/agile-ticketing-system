# agile-ticketing-system

**A Ticket management System.**

## Installation steps

1> Clone the repository

```
git clone https://github.com/rajpatel24/agile-ticketing-system.git
```

2> Create virtualenv

```
virtualenv -p python3.6 venv

source venv_myblog/bin/activate
```

3> Install dependencies

```
pip install -r requirements.txt
```

4> Create local.py file

```
cp agile-ticketing-system/agile-ticketing-system/settings/example-production.py agile-ticketing-system/agile-ticketing-system/settings/local.py
```

5> Run migrations (Go to `project root` folder)

```
python manage.py makemigrations
python manage.py migrate
```

6> Run the project

```
python manage.py runserver
```
