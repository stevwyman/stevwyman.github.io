<!-- Top Navigation -->
* [Psychology](/psycholgy.md)
* [Game Theory](/game_theory.md)
* *Web Development*
    * [Python](/wd-python.md)
    * [CSS](/wd-css-notes.md)
    * [SQL](/wd-sql.md)
* [Web Dev](/web-dev.md)


# Web Development

This section is focussed on web development using python, sql, js and django


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