# CSS Concepts:

Cascading Style Sheets:
A CSS rule-set consist of a selector and a declaration block

example:
```
    h1          { color: blue; font-size: 12px;}
(selector)                   (body)

```


## CSS Box Model:
All HTML elements can be considered as boxes. In CSS, the term "box modeel" is used
when talking about design and layout.

The CSS box model is essentially a box that wraps around every HTML element. It
consist of: (Margin (Border (Padding (content)))).

+----------------------------------------+
|                 Margin                 |
| +------------------------------------+ |
| |               Border               | |
| |   +------------------------------+ | |
| |   |           Padding            | | |
| |   |  +-------------------------+ | | |
| |   |  |        content          | | | |
| |   |  +-------------------------+ | | |
| |   |                              | | |
| |   +------------------------------+ | |
| +------------------------------------+ |
+----------------------------------------+


An example of the box model:
```
div {
  width: 300px;
  border: 15px solid green;
  padding: 50px;
  margin: 20px;
}
```



--------------------------------------------------

## Element selector: 

You can select all &lt;h1&gt; elements or all &lt;p&gt; elements on a page like this:

To set style for all the &lt;h1&gt; tags:

```
h1    {
         text-align: center;
         color: red;
      }
```

--------------------------------------------------

## Id Selector:

Uses the id attribute of the html element to select a specific element.

```
#para1   {
            text-align: center;
            color: red;
         }
```
--------------------------------------------------

## Class selector:

The class selector selects elements with a specific class attribute.

```
.center   {
             text-align: center;
             color: red;
          }
```
--------------------------------------------------

## Class and Element selector:

You saw the three ways we can identify elements in our html code
and apply specific styles. 

EG: Say you want to apply a style to all  &lt;p&gt; elements with class "para1" like below:

```
p.para1   {
             text-align: center;
             color: red;
          }

```
--------------------------------------------------

## Grouping selectors to optimize code:

consider example below

```
h1 {
    text-align: center;
    color: red;
}

p {
    text-align: center;
    color: red;
}
```

**This can be written as:**

```
h1, p {
    text-align: center;
    color: red;
}

```

## More Complex element selections:

### Selecting an element with multiple classes

Consider these elements:

```
<h2 class="test3 test4">This is test3 and test4</h2>
<h2 class="test3"> Thi sis test3 only</h2>
```

**To select the element with classes test3 and test4:**

This will select only the first h2 element with both classes

```
.test3.test4 {
    color: green;
}

```

### Selecting multiple items/elements with their own class

Consider two  elements as below:

```
<h1 class="test4">This is test4</h1>
<h2 class="test3"> Thi sis test3 only</h2>
```

**To select both these elements:**

```
.test3, .test4 {
    color: red;
}

```


### Selecting element from specific parent.

Consider below example:

```
<div class="test0">
    <h2 class="test1">This is test1</h2>
</div>
<h2 class="test1"> This is test1 outside div</h2>

```

**To select the element h2 in div class test0:**

```
.test0 .test1 {
    color: white;
}

```



--------------------------------------------------

## Inserting CSS:

Three ways to do that:
  1. external style sheet
  2. Internal style sheet
  3. Inline style


**External:**

```
<head>
  <link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```


**Internal:**

```
<head>
  <style>
    body {
      background-color: linen;
    }

    h1 {
      color: maroon;
      margin-left: 40px;
    }  
  </style>
</head>
```


**Inline:**

```
<h1 style="color:blue;margin-left:30px;">This is a heading.</h1>
```


> **NOTE:**  
> If some property has been defined for the same selector (element) 
> in different style sheets, the value from the last read style sheet
> will be used.

--------------------------------------------------

## CSS Pseudo class selector (:not())

:not() is a CSS negation pseudo-class selector. It is a functional 
pseudo-class selector that will take a regular selecto as an argument,
and then match any elements that are not represented by the argument.

:not() takes as an argument any of the following:
* Element selector (eg: p, span, div, etc.)
* Class selector (eg: .sidebar, .col_m1, etc.)
* ID selector (eg: #custom)
* Attribute selector (eg [type="checkbox"])
* Universal selector ```(*)```

**Note:** The argument passed to :not() cannot be a pseudo-element selector
such as (::before and ::after) or any other pseudo-class selector.

Example Usages:

```
li:not(.new) {
    /* Style all list elements except the ones that have class 'new' */
}
```

The :not() selector is chainable with more :not() selectors.
Example:

```
li:not(#feature):not(.tutorial) {
    /* Style all list elements that do not have feature flag, and that
       do not have class tutorial
    */
}
```

You can also use the :not() selector globally, without applying it to 
any elment, thus selecting all elements in a document that are not represented
in the argument.

```
:not(a) {
    color: #333;
}
```

The specificity of :not() pseudo-class is the specificity of it's argument.
:not() does not add to the selector specificity unlike other pseudo-classes.


--------------------------------------------------

## Cascading order:

What style will be used when there is more than one style specified for an HTML element?

We say the styles will "cascade" into a new "virtual" style sheet by folling rules.

**Priority:**

  1. Inline style (inside the HTML element)
  2. External and internal style sheets (in head section)
  3. Browser default

--------------------------------------------------

## CSS Specificity:

Another import concept to learn in css is different selectors have different
specificity values.

This is an important concept when you are trying to figure out which style
will be picked when you are trying to override.

Here is the list from most specificity value to least specifity value:

* Style attribute - If the element has inline styling, that automatically wins.
  (1,0,0,0 points)
* ID - For each ID value, apply (0,1,0,0 points)
* Class, pseudo-class or attribute selector - add (0,0,1,0 points)
* For each element reference apply (0,0,0,1 point)

You can read the values as numbers, however these are not base 10 system.

Examples:

ul#nav li.active a - (Style attribute, ID, class, Elements)
    Points:          (      0,          1,   1,      3    )


body.ie7 .col_3 h2 ~ h2 - (Style attribute, ID, class, Elements)
    Points:               (   0,            0,    2,     3     )


--------------------------------------------------

## Additional Links

Color mapper:
http://www.w3schools.com/css/css_colors.asp

3d button:
http://css3button.net/

3d html:
http://keithclark.co.uk/articles/creating-3d-worlds-with-html-and-css/

[css3 brradshawenterprises](http://css3.bradshawenterprises.com/transitions/)

--------------------------------------------------



