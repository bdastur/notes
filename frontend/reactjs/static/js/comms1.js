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
 * Example of component communicating to code residing outside
 * the component
 */

class Text extends React.Component {
  constructor (props) {
    super(props);
    this.state = {text: "Dummy1"};
  }

  onChangeHandle = (e) => {
    this.setState({text: e.target.value});
    handleInput(e.target.value);
    someFunc(e.target.value);
  }

  render () {
    let label = React.createElement("h4", null, this.state.text)
    let input = React.createElement("input",
                                    {onChange: this.onChangeHandle}, null);
    let div = React.createElement("div", null, label, input);
    return (div);
  }
}

function someFunc(text) {
  console.log("someFunc: " + text);
}

/*
 * This function get invoked from the component, and it sets a 
 * text for div
 */
handleInput = (text) => {
  console.log("Handle input: " + text);
  div = document.getElementById("text");
  div.innerHTML = text;
}


let text = React.createElement(Text, null, null);
ReactDOM.render(text, document.getElementById("root"));

