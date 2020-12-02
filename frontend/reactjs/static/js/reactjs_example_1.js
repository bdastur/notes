/*
 * Each JSX element is just syntactic sugar for calling 
 * React.createElement(component, props, ...children). 
 * So, anything you can do with JSX can also be done with just 
 * plain JavaScript.
 *
 * https://reactjs.org/docs/react-api.html#createelement
 */

class MyForm extends React.Component {
    constructor (props) {
        super(props);
        this.state = { name: ''};
    }
 
    myChangeHandler = (event, value) => {
        console.log(value);
        this.setState({name: event.target.value});
    }
  
    render () {
        const header_style = {
            color: "white",
            backgroundColor: "DodgerBlue",
            padding: "10px",
            fontFamily: "Arial"
        }
        let elem_header = React.createElement(
            "h1", {style: header_style}, "Name: ",  this.state.name);
        let elem_para = React.createElement(
            "p", null, "Enter your name:");
        let elem_input = React.createElement(
            "input", {type: "text", onChange: this.myChangeHandler});
        let elem_form = React.createElement(
            "form", null, elem_header, elem_para, elem_input);
        let elem = React.createElement(
            "div", null, 
            "Hello", 
            "Oh yeah! ", this.props.toWhat,
            elem_form);
        return (
            elem
        );
    }
}

ReactDOM.render(
    React.createElement(MyForm, {toWhat: 'Hey Ho World'}, null), 
    document.getElementById('root'));
