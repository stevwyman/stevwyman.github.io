---
- [Game Theory](/game_theory.md)
   - [Negotiations](/negotiations.md)
- [Python](/python.md)
- [Web Dev](/web-dev.md)
   - [CSS](/css.md)
---

# Notes on CSS
<a name="css-top"></a>

Some notes on css ...

---
- [Addressing](#addressing-elements)
- [Responsiveness](#responsiveness)
- [SASS](#sass)
---

## Addressing elements
<a name="addressing-elements"></a>

inline

id

class

type

either by name, such as th, td, ..
by unique identifier, such as id and then use the # in css
by class and then in use the . in css

### Identifying elements

* div
* span
* id
* class

### Specificity

This specifies the priority of the different ways styles can be asserted to attributes. Inline properties will always have the highest priority, regardless if they have an id or a class associated with the in a style-sheet.

1. inline
2. id
3. class
4. type

### CSS Selectors

use the below selectors to assign styles to specific attributes

| use in css | Selector |
|--|--|
|a, b|Multiple Element|
|a b|Descendant|
|a>b|Child|
|a+b|Adjacent Sibling|
|[a=b]|Attribute|
|a:b|Pseudoclass|
|a::b|Pseudoelement|

The below redes only list items, that are children from an unordered list in blue:

```html
<style>
    ul > li {
        color: blue;
    }
</style>
```

or

Color only one link

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>My Web Page!</title>
        <style>
            a {
                color: blue;
            }

            a[href="https://facebook.com"] {
                color: red;
            }
        </style>
    </head>
    <body>
        <ul>
            <li><a href="https://google.com">Google</a></li>
            <li><a href="https://facebook.com">Facebook</a></li>
            <li><a href="https://amazon.com">Amazon</a></li>
        </ul>
    </body>
</html>
```

<p align="right">(<a href="#css-top">back to top</a>)</p>

---

## Responsiveness
<a name="responsiveness"></a>

media query using @media (min-width) make background red

Flexbox:
#container {
display: flex;
flex-wrap: wrap;
}

#container > div {
background-color: springgreen;
font-size: 20px;
margin: 20px;
}

### Flexbox

```css
<style>
    .container {
        display: flex;
        flex-wrap: wrap;
    }

    .container > div {
        background-color: springgreen;
        font-size: 20px;
        margin: 20px;
        padding: 20px;
        width: 200px;
    }
</style>
```

### Grid Layout

```css
<style>
    .grid {
        background-color: green;
        display: grid;
        padding: 20px;
        grid-column-gap: 20px;
        grid-row-gap: 10px;
        grid-template-columns: 200px 200px auto;
    }

    .grid-item {
        background-color: white;
        font-size: 20px;
        padding: 20px;
        text-align: center;
    }
</style>
```

<p align="right">(<a href="#css-top">back to top</a>)</p>

---

## SASS
<a name="sass"></a>

With sass, we can apply some basic coding principles to css. This can help ba **inherit** attributes and to group attributes.

Usage:

```sh
sass source.scss:target.css
```

<p align="right">(<a href="#css-top">back to top</a>)</p>

---
