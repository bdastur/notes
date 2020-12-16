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
 * Here two sibling components communicate.
 * Text component has an input, when this is changed, it updates
 * label of Text2 component.
 *
 * This builds on the comms.js model, with one addition of a
 * function bind in Text2 component
 */

class Text extends React.Component {
  constructor (props) {
    super(props);
    this.state = {text: "Dummy1"};
  }

  onChangeHandle = (e) => {
    this.setState({text: e.target.value});
    handleInput(e.target.value);
  }

  render () {
    console.log("Text -- Render");
    let label = React.createElement("h4", null, this.state.text)
    let input = React.createElement("input",
                                    {onChange: this.onChangeHandle}, null);
    let div = React.createElement("div", null, label, input);
    return (div);
  }
}

function handleInput(text) {
  this.setState({'text': text});
}

class Text2 extends React.Component {
  constructor (props) {
    super(props);
    this.state = {'text': "Text 2 - Dummy"};
    handleInput = handleInput.bind(this);
  }

  render () {
    let label = React.createElement("h4", null, this.state.text)
    let div = React.createElement("div", null, label);
    return (div);
  }
}


let text = React.createElement(Text, null, null);
let text2 = React.createElement(Text2, null, null);
ReactDOM.render(text, document.getElementById("root"));
ReactDOM.render(text2, document.getElementById("text2"));

