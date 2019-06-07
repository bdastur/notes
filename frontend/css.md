# CSS Concepts:

Cascading Style Sheets:
A CSS rule-set consist of a selector and a declaration block

example:
```
    h1          { color: blue; font-size: 12px;}
(selector)                   (body)

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

## Cascading order:

What style will be used when there is more than one style specified for an HTML element?

We say the styles will "cascade" into a new "virtual" style sheet by folling rules.

**Priority:**

  1. Inline style (inside the HTML element)
  2. External and internal style sheets (in head section)
  3. Browser default


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



