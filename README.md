# Demo web site in Django with implementation of simple user authorization scheme

# Added API */api/version/* to show application details in the following form:

```
{
    "commit": "ebed9221e0b4787a400622919cf34459a0b51b77",
    "branch": "master",
    "commit_date": "2019-05-25T08:33",
    "version": "release_v1.16.2",
    "started": "2019-05-25T08:34:18",
    "uptime_seconds": 2
}
```

Version of the application must be stored in the _version file in the project root directory



# Run application
```
python manage.py runserver