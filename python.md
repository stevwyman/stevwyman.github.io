<!-- Top Navigation -->
* [Psychology](/psycholgy.md)
* [Game Theory](/game_theory.md)
* *Python*
* [Web Dev](/web-dev.md)
   
---

## Python Tool Kit

Some helpful tools when developing using python. Even though python is made for quick and dirty hacking, there is also a way to somehow properly write code which is readable and maintainable. THe two tools below can help with that.

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
````
def greet1(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
```

