# ReactJS

## Useful links:
* [React top-level api](https://reactjs.org/docs/react-api.html)
* [ReactDOM](https://reactjs.org/docs/react-dom.html)


## React Component

`React.Component`
React components let you split the UI into independent, reusable pieces, and
think about each piece in isolation. React components can be defined by subclassing
React.Component or React.PureComponent.

## A simple React component:

This is the most basic react component. The class `Banner` extends React.Component.
The only method that is required in a React.Component subclass is render().
All other methods are optional.

```
class Banner extends React.Component {
  render () {
    let textElement = React.createElement("h1", null, "Behzad");
    return textElement;
  }
}
```

To render and display this component on the brower, you will need to use the
ReactDom's render method as below.

```
let welcomeObj = React.createElement(Banner, null, null);
ReactDOM.render(welcomeObj, document.getElementById("root"));
```


## The createElement() API:
Create and return a new React element of the given type. The type argument can be
either a tag name string (such as 'div' or 'span'), a React component
type (a class or a function), or a React fragment type.


```
React.createElement(
  type,
  [props],
  [...children]
)
```


## Updating a Rendered Element.
* React elements are immutable. Once you create an element, you
  cannot change it's children or attributes.
* An element represents the UI at a certain point in time.

## The ReactDOM.



## Adding event handler.
An event handler is a prop

```
class Banner extends React.Component {
  clickHandler = (event, data) => {
    alert(event.target.outerText);
  }

  render () {
    let textElement = React.createElement("h1",
                                          {onClick: this.clickHandler},                                                     "Behzad");
    return textElement;
  }
}

let welcomeObj = React.createElement(Banner, null, null);
ReactDOM.render(welcomeObj, document.getElementById("root"));
```


### Updating React element (regular interval)
here is an example of updating a text at regular intervals.

```
class Banner extends React.Component {

  render () {
    let randomNumber = Math.floor(Math.random() * 5);
    let textElement = React.createElement("h1",
                                          null,                                                     randomNumber);
    return textElement;
  }
}

function tick() {
  let welcomeObj = React.createElement(Banner, null, null);
  ReactDOM.render(welcomeObj, document.getElementById("root"));
}

setInterval(tick, 3000);

```

### Props.
When you define a React element, you would notice that you can pass
attributes to the element. In React this object is called  'Props'. It is
the second argument of React.createElement() method.

* A note about props: They are Read-Oly.

```
class Banner extends React.Component {
  render () {
    let randomNumber = Math.floor(Math.random() * 5);
    let textElement = React.createElement("H2",
                                          {class: this.props.elem_class,
                                           onClick: this.clickHandler},
                                           this.props.message);
    return textElement;
  }
}

let bannerProps = {
  message: "This is a test message",
  elem_class: "text-3xl text-blue-500"
}

let welcomeObj = React.createElement(Banner, bannerProps, null);
ReactDOM.render(welcomeObj, document.getElementById("root"));
```


### Parent/Child elements.
Most times you will have a container element, that includes other
child elements.
Like a Grid element that can have multiple child elements.
An example below shows such a scenario:

--Sibling to parent communication--
* The Grid element passes a 'callback' prop to the child element in
  it's render() method.
* The child element 'banner' has a clickHandler() method that is invoked
  whenever it is clicked. It calls the parent callback here.
  `this.props.callback(data)`

```
function siblingHandler(text) {
  this.setState({'message': text});
  alert("Sibling handler: " + text);
}

/*
 * createElement.
 * React.createElement(type, [props], [...children])
 */
class Banner extends React.Component {
  constructor (props) {
    super(props);
    siblingHandler = siblingHandler.bind(this);
  }
  clickHandler = (event, data) => {
    console.log("CLicked: " + event.target.outerText);
    console.dir(event.target);
    alert(event.target.outerText);
    this.props.callback(event.target.outerText);
    siblingHandler(event.target.outerText);
  }

  render () {
    let randomNumber = Math.floor(Math.random() * 5);
    let textElement = React.createElement("H2",
                {class: this.props.elem_class, onClick: this.clickHandler},                               this.props.message);
    return textElement;
  }
}

class Grid extends React.Component {

  childCallback = (value) => {
    alert("child value: " + value);
  }

  render () {
    let prop = {
      message: "This is a test",
      elem_class: "text-3xl text-blue-500 border p-2",
      callback: this.childCallback
    };
    let bannerHello = React.createElement(Banner,prop, null);

    prop = {
      message: "Welcome",
      elem_class: "text-3xl text-blue-500 border p-2",
      callback: this.childCallback
    };

    let bannerWelcome = React.createElement(Banner, prop, null);

    let gridElem = React.createElement("div",
          {class: "grid grid-cols-3 gap-2 m-4 p-4 border border-t-8 border-blue-600"},
          bannerHello, bannerWelcome);
    return gridElem;
  }
}

let gridObj = React.createElement(Grid, null, null);
ReactDOM.render(gridObj, document.getElementById("root"));
```
