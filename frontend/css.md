# CSS Concepts:

## Links:
[W3C Css validation service](https://jigsaw.w3.org/css-validator/)
[Mozilla Web Docs: CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

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

```
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
```


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

## Attribute selector:

With attribute selector you can select all elements that have a specific
attribute.

For example:
```
<button>Enabled</button>
<button disabled="true">Disabled</button>
```

Here we define an attribute selector target, putting it within []. In this case
all elements with disabled attribute will get the properties.

```
[disabled] {
	background-color: #242620;
	color: #ffffff;
	border-color: black;
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


### Selecting element from specific parent. (Descendant combinator)
*Note:* This is also called a descendant combinator.
In this case .test1 is a descendant of .test0, it does not have to be a direct
child.

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

### Adjacent sibling combinator

Consider the below html snippet.
```
<div class="section3">
   <h2>Child 1</h2>
   <p>This is a child 1</p>
   <h2>Child 2</h2>
   <p>This is a second child</p>
   <span>This is a span</span>
   <p>Paragraph after span</p>
</div>

```

If I wanted to select all the 'p' paragraph elements here, I can use a
target selector as below. Which tells is to select all 'p' elements 
immediately follwoing 'h2' element. It will not select the last 'p' element 
following the 'span'

```
h2 + p {
	color: green;
}
```

We can get even more specific and say select only 'p' elements which are 
immediately follwed by 'h', and are a within our 'div section' as below:

```
.section3 > h2 + p {
	color: green;
}
```


### General sibling combinator


### Child combinator


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

## CSS Pseudo classes:

[pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)

A CSS pseudo-class is a keyword added to a selector that specifies a special
state of the selected elements. 

For example :hover can be used to change a buttons color when user's pointer
hovers over it.

```
button:hover {
  color: blue;
}

```

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

## Pseudo-class selector :empty

An element counts as empty if it doees not have any child elements (nodes)
or text content. 

Examples::
```
<div><!-- Comment heree --></div>

```

The above div has no text or element and hence is empty.


```
<p> </p>
```

Above p element is not empty, as white spaces are considered content.

```
<hr />, <br />, <img />
```
Above self-closing elements are considered empty.



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

## CSS Custom properties:

[Mozilla.org custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)
Often times we want to specify the same property values to multiple 
elements in an html page. 

CSS Custom properties are a way to achive that. These values can be defined and
reused throught the document. They are set using custom property notation.
eg: (--body-bg-color: green), and are accessed using the var() function.
eg: ( color: var(--body-bg-color).

Custom properties are subject to the cascade and inherit their value from their parent.


```
:root {
	--body-bg-color: #e8edda;
	--textarea-bg-color: #c6c1bb;
}

body {
	font-family: 'Roboto', sans-serif;
	background-color: var(--body-bg-color);
}

textarea {
	font-family: sans-serif;
	resize: none;
	background-color: var(--textarea-bg-color);
}

```

### Fallback values.
Using the var() function, you can define multiple fallback values when the
given variable is not yet defined.

*Note*: Fallback values aren't used to fix browser compatibility. If the browser
does not support CSS custom properties, the fallback values will not help.

The first argument to the function is the name of the custom property, the
second argument if provided is the fallback value. The var() function accepts
only two parameters, assiging everything following the first comma as the
second parameter.

Example:
here the --textarea-bg-color is not defined, so the fallback is 'grey'

```
:root {
	--body-bg-color: #e8edda;
}

textarea {
	font-family: sans-serif;
	resize: none;
	background-color: var(--textarea-bg-color, grey);
}
```

--------------------------------------------------

## CSS inheritence


When no value for an inherited property has been specified on an element, 
the element gets the computed value of that property on its parent element. 
Only the root element of the document gets the initial value given in the
property's summary.

When no value for a non-inherited property has been specified on an element, 
the element gets the initial value of that property (as specified in the 
property's summary).

In this example, the first 'h1' element will inherit font-family from the body,
since it is not specified in the h1 target selector, while the second h1 elemeent 
will get the font sans-serif as it is defined in it's class selector

```
body {
	font-family: 'Roboto', sans-serif;
	background-color: var(--body-bg-color);
	margin-left: 15px;
}

h1 {
    color: red;
}

.blue-header {
	color: blue;
	font-family: sans-serif;
}

<h1>CSS Example 1</h1>
<h1 class="blue-header">CSS Example (with style)</h1> 

```

--------------------------------------------------

## CSS Animation and Transitions


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



