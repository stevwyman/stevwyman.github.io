<!-- Top Navigation -->
* [Psychology](/psycholgy.md)
* [Game Theory](/game_theory.md)
* [Web Development](/web-dev.md)
    * *Python*
    * [CSS](/wd-css-notes.md)
    * [SQL](/wd-sql.md)
   
---

## Python Tool Kit

Some helpful tools when developing using python. Even though python is made for quick and dirty hacking, there is also a way to somehow properly write code which is readable and maintainable. THe two tools below can help with that.

### unit test

```py
import unittest

from prime import is_prime

class Tests(unittest.TestCase):

    def test_1(self):
        """Check that 1 is not prime."""
        self.assertFalse(is_prime(1))
```

### pytest

You can check your implementation by providing test specification and run pytest. THe following examples demonstrate:

* you need to import the class or method which you would like to test
* use assert to check for equality
* use assert together with approx when you have float
* check if an error is raised and that the error message matches

```sh
import pytest
from game import (
    Strategy,
    all_entries_equal,
    is_biggest_in_list,
    minimaxi,
    oddments2,
)

def test_minimaxi():
    s_01 = Strategy("S_01", (9, 7))
    s_02 = Strategy("S_02", (5, 11))
    strategy_set = list()
    strategy_set.append(s_01)
    strategy_set.append(s_02)

    assert minimaxi(strategy_set) == (7, 9)

def test_oddments2():
    # wrong number of strategies in the set
    s_01 = Strategy("S_01", (0, 0))
    strategy_set = list()
    strategy_set.append(s_01)

    with pytest.raises(ValueError) as e_info:
        oddments2(strategy_set)
    assert str(e_info.value) == "Strategy set must have a length of 2"

def test_formula_2x2():
    # tax payers example
    s_01 = Strategy("S_01", (2, 4))
    s_02 = Strategy("S_02", (4, 0))
    strategy_set = list()
    strategy_set.append(s_01)
    strategy_set.append(s_02)

    assert formula_2x2(strategy_set)[0] == pytest.approx(2 / 3)
    assert formula_2x2(strategy_set)[1] == pytest.approx(1 / 3)
```

### mypy

use mypy to check annotations and ensure types are consistent

```sh
$ mypy foo.py bar.py some_directory
```

Within your python code, you might want to hint of what type your variables are. You can do this in the way below:

```python
class Game:
    def __init__(self, player: Player, opponent: Player):
        self._player = player
        self._opponent = opponent
        self._players = [self._player, self._opponent]
```

and within your method, or declaration you can use the following:

```python
    def pure_nash_equilibrium(self) -> list[tuple[Strategy, Strategy]]:
    
        nash_equilibria: list[tuple[Strategy, Strategy]] = list()
        opponent_strategy_set: list[Strategy] = self._opponent.strategy_set
        player_strategy_set: list[Strategy] = self._player.strategy_set
```

## web

### Django

#### testing

python manage.py test

> Note: this test will create a new database and destroys it afterwards

```py
from django.test import Client, TestCase

# Create your tests here.
class FlightTestCase(TestCase):

    def setUp(self):

        # Create airports.
        a1 = Airport.objects.create(code="AAA", city="City A")
        a2 = Airport.objects.create(code="BBB", city="City B")

        # Create flights.
        Flight.objects.create(origin=a1, destination=a2, duration=100)
        Flight.objects.create(origin=a1, destination=a1, duration=200)
        Flight.objects.create(origin=a1, destination=a2, duration=-100)

    def test_departures_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(), 3)
```

for testing web functionality you might want to use selenium

#### some commands

pip3 install Django

django-admin startproject PROJECT_NAME

python manage.py runserver

python manage.py startapp APP_NAME

#### structure

* manage.py: utility for interacting with project 
* PROJECT_NAME/settings.py: settings and configuration 
    * add here the app you would like to install
* PROJECT_NAME/urls.py: URLs that can be visited
    * example: path("tasks/", include("tasks.urls")),

under APP_NAME/urls.py, using path("<str:name>", views.greet1, name="greet"), you can take the url as parameter input

under APP_NAME/views.py, using

```py
def greet1(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
```

#### models

Django Models are a level of abstraction on top of SQL that allow us to work with databases using Python classes and objects rather than direct SQL queries.

Let’s get started on using models by creating a django project for our airline, and creating an app within that project.

```sh
django-admin startproject airline
cd airline
python manage.py startapp flights
````

Now we’ll have to go through the process of adding an app as usual:

1. Add flights to the INSTALLED_APPS list in settings.py
2. Add a route for flights in urls.py:
    ```path("flights/", include("flights.urls")),```
3. Create a urls.py file within the flights application. And fill it with standard urls.py imports and lists.
Now, rather than creating actual paths and getting started on views.py, we’ll create some models in the models.py file. In this file, we’ll outline what data we want to store in our application. Then, Django will determine the SQL syntax necessary to store information on each of our models. Let’s take a look at what a model for a single flight might look like:

```py
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()
````

Let’s take a look at what’s going on in this model definition:

* In the first line, we create a new model that extends Django’s model class.
* Below, we add fields for origin, destination, and duration. The first two are Char Fields, meaning they store strings, and the third is an Integer Field. These are just two of many built-in Django Field classes
* We specify maximum lengths of 64 for the two Character Fields. you can check the specifications available for a given field by checking the documentation.

#### Migrations

Now, even though we’ve created a model, we do not yet have a database to store this information. to create a database from our models, we navigate to the main directory of our project and run the command.

```sh
python manage.py makemigrations
````

This command creates some Python files that will create or edit our database to be able to store what we have in our models. You should get an output that looks something like the one below, and if you navigate to your migrations directory, you’ll notice a new file was created for us

migrations output 0

Next, to apply these migrations to our database, we run the command

```sh
python manage.py migrate
```

Now, you’ll see some default migrations have been applied along with our own, and you’ll also notice that we now have a file called db.sqlite3 in our project’s directory

migrate output

#### Shell

Now, to begin working adding information to and manipulating this database, we can enter Django’s shell where we can run Python commands within our project.

python manage.py shell
Python 3.7.2 (default, Dec 29 2018, 00:00:04)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.
# Import our flight model
In [1]: from flights.models import Flight

# Create a new flight
In [2]: f = Flight(origin="New York", destination="London", duration=415)

# Instert that flight into our database
In [3]: f.save()

# Query for all flights stored in the database
In [4]: Flight.objects.all()
Out[4]: <QuerySet [<Flight: Flight object (1)>]>
When we query our database, we see that we get just one flight called Flight object (1). This isn’t a very informative name, but we can fix that. Inside models.py, we’ll define a __str__ function that provides instructions for how to turn a Flight object into a string:

class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
Now, when we go back to the shell, our output is a bit more readable:

# Create a variable called flights to store the results of a query
In [7]: flights = Flight.objects.all()

# Displaying all flights
In [8]: flights
Out[8]: <QuerySet [<Flight: 1: New York to London>]>

# Isolating just the first flight
In [9]: flight = flights.first()

# Printing flight information
In [10]: flight
Out[10]: <Flight: 1: New York to London>

# Display flight id
In [11]: flight.id
Out[11]: 1

# Display flight origin
In [12]: flight.origin
Out[12]: 'New York'

# Display flight destination
In [13]: flight.destination
Out[13]: 'London'

# Display flight duration
In [14]: flight.duration
Out[14]: 415
This is a good start, but thinking back to earlier, we don’t want to have to store the city name as an origin and destination for every flight, so we probably want another model for an airport that is somehow related to the flight model:

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
We’ve seen everything in our new Airport class before, but the changes to the origin and destination fields within the Flight class are new to us:

We specify that the origin and destination fields are each Foreign Keys, which means they refer to another object.
By entering Airport as our first argument, we are specifying the type of object this field refers to.
The next argument, on_delete=models.CASCADE gives instructions for what should happen if an airport is deleted. In this case, we specify that when an airport is deleted, all flights associated with it should also be deleted. There are several other options in addition to CASCADE.
We provide a related name, which gives us a way to search for all flights with a given airport as their origin or destination.
Every time we make changes in models.py, we have to make migrations and then migrate. Note that you may have to delete your existing flight from New York to London, as it doesn’t fit in with the new database structure.

# Create New Migrations
python manage.py makemigration

# Migrate
python manage.py migrate
Now, let’s try these new models out in the Django shell:

# Import all models
In [1]: from flights.models import *

# Create some new airports
In [2]: jfk = Airport(code="JFK", city="New York")
In [4]: lhr = Airport(code="LHR", city="London")
In [6]: cdg = Airport(code="CDG", city="Paris")
In [9]: nrt = Airport(code="NRT", city="Tokyo")

# Save the airports to the database
In [3]: jfk.save()
In [5]: lhr.save()
In [8]: cdg.save()
In [10]: nrt.save()

# Add a flight and save it to the database
f = Flight(origin=jfk, destination=lhr, duration=414)
f.save()

# Display some info about the flight
In [14]: f
Out[14]: <Flight: 1: New York (JFK) to London (LHR)>
In [15]: f.origin
Out[15]: <Airport: New York (JFK)>

# Using the related name to query by airport of arrival:
In [17]: lhr.arrivals.all()
Out[17]: <QuerySet [<Flight: 1: New York (JFK) to London (LHR)>]>


