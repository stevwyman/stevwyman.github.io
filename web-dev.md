<!-- Top Navigation -->
* [Psychology](/psycholgy.md)
* [Game Theory](/game_theory.md)
* *Web Development*
    * [Python](/wd-python.md)
    * [CSS](/wd-css-notes.md)
    * [SQL](/wd-sql.md)


# Web Development


This section is focussed on web development using python, sql, js and django

## git

to switch between branches

```sh
git branch
git checkout <selected-branch>
```

to create a new branch to work on new feature use the 
```sh
git checkout -b ＜new-branch＞
```

### git actions

running workflows, specified in YAML

````
name: Testing
on: push

jobs:
  test_project:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Run Django unit tests
      run: |
        pip3 install --user django
        python3 manage.py test

````

## Docker

Dockerfile
````
FROM python:3
COPY .  /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
````

```sh
docker build -t <image> <path to Dockerfile>
```

to run the above image and be able to access port 8000 from the host use:

```sh
docker run -p 8000:8000 <image>
```

docker-compose.yml

````
version: '3'

services:
    db:
        image: postgres

    web:
        build: .
        volumes:
            - .:/usr/src/app
        ports:
            - "8000:8000"

````

with 
```sh
docker ps
``` 
we can list the docker container and then with the container id we can access the app
```sh
docker exec -it <id> bash -l
```

### Pitfalls

There are some tricky pitfalls when working with docker:

* make sure the target architecture matches
* no deployment using docker import/export as this is dropping CMD or ENTRYPOINT metadata information, especially when using plesk
    * manually cp/ftp/... image to remote server and use the docker load
    * use dockerhub
* before pushing your image to the hub, you need to tag it
    * docker tag firstimage YOUR_DOCKERHUB_NAME/firstimage
    * docker push YOUR_DOCKERHUB_NAME/firstimage

## JavaScript

access dom elements

* document.querySelector('tag')
* document.querySelector('#id')
* document.querySelector('.class')

Local Storage

* localStorage.getItem(key) 
* localStorage.setItem(key, value)

```js
<script>
    document.addEventListener('DOMContentLoaded', () => {

        // Change the color of the heading when dropdown changes
        document.querySelector('#color-change').onchange = function() {
            document.querySelector('#hello').style.color = this.value;
        };

    });
</script>
```