/*
 * Each JSX element is just syntactic sugar for calling
 *
 * React.createElement(component, props, ...children).
 * So, anything you can do with JSX can also be done with just
 * plain JavaScript.
 *
 * https://reactjs.org/docs/react-api.html#createelement
 *
 * ReactDOM.render(element, container[, callback])
 */

/*
 * This example shows both. 
 * 1. A parent to child communication mechanism, and
 * 2. A child to parent communication.
 * 1.
 * Here a parent updates the child state.
 *   - A global function 'updateChild' is defined. 
 *   - Then in child component constructor create a bind to this func.
 *   - Define a onChange handler for input element in parent, which
 *     calls the 'updateChild' function - which updates the child state.
 *
 * 2.
 * Here a child updates the parent state. The way this is handled here is
 * the parent sends a callback function as props.
 * - Parent defines a functionn 'childCallback'.
 * - Passes this function as a callback to the child using props.
 * - The child component's input element registeres the onChange 
 *   handler 'updateChildLabel', which calls 'this.props.callback'
 *
 * This builds on the sibling_comms.js mode
 */

function updateChild (data) {
    this.setState({text: data});
}

class Child extends React.Component {
  constructor (props) {
    super(props);
    this.state = {text: "Child - Dummy1"};
    updateChild = updateChild.bind(this);
  }

  updateChildLabel = (e) => {
    console.log("Update child label");
    this.props.callback(e.target.value);
  } 

  render () {
    console.log("Text -- Render");
    let input = React.createElement("input",
                                   {onChange: this.updateChildLabel}, null);
    let label = React.createElement("h4", null, this.state.text)
    let div = React.createElement("div", null, input, label);
    return (div);
  }
}


class Parent extends React.Component {
  constructor (props) {
    super(props);
    this.state = {'text': "Parent"};
  }

  updateText =  (e) => {
    updateChild(e.target.value);
  }

  childCallback = (data) => {
    console.log("Child callback!");  
    this.setState({text: data});
  }

  render () {
    let child_props = {
      callback: this.childCallback
    }

    let child = React.createElement(Child, child_props, null);
    let label = React.createElement("h4", null, this.state.text)
    let input = React.createElement("input",
                                    {onChange: this.updateText}, null);
     let div = React.createElement("div", null, child, label, input);
    return (div);
  }
}


let parent = React.createElement(Parent, null, null);
ReactDOM.render(parent, document.getElementById("root"));

