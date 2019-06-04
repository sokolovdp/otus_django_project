# Demo web site in Django with implementation of simple user authorization scheme and API to get current application version

## Run application
```
python manage.py runserver
```
Django server will start at localhost:8000/


## To load initial data into DB run:
```
python manage.py loaddata ./main_app/fixtures/items.json

```

##  To get version number API: GET /api/version/
```
{
    "commit": "1a2623f8f85fdb680a8be43956e1c767c59256a9",
    "branch": "master",
    "commit_date": "2019-05-29T17:02:03",
    "version": "0.2",
    "started": "2019-05-31T08:44:21",
    "uptime_seconds": 4
}
```