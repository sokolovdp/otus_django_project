# Demo web site in Django with implementation of simple user authorization scheme

# Added API */api/version/* to show application details in the following form:

```
{
    "commit": "dbd20ca61f2a0770a6465dec0a5108bedd17819a",
    "branch": "master",
    "commit_date": "2019-05-25T08:55:13Z",
    "version": "release_v1.16.2",
    "started": "2019-05-25T09:22:21",
    "uptime_seconds": 7
}
```
1) Time is shown in GMT format

1) Version of the application must be stored in the **_version** file in the project root directory
2) In **settings.py** was added the following code:

```

repo = Repo()
active_branch = repo.active_branch.name
head_commit = repo.heads.master.commit
start_time = datetime.now().replace(microsecond=0)

with open('_version', 'rt') as version_file:
    _version = version_file.readline().strip()

APPLICATION_VERSION = {
    "commit": str(head_commit),
    "branch": str(active_branch),
    "commit_date": time.strftime("%Y-%m-%dT%H:%M", time.gmtime(head_commit.committed_date)),
    "version": _version,
    "started": start_time
}
```



# Run application
```
python manage.py runserver