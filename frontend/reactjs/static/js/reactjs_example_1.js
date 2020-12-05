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
 <div class="grid-layout-1 c3">
            <div class="gelem c1c4 r1r2 colored">One</div>
            <div class="gelem c1c2 r2r4 colored">Two</div>
            <div class="gelem c2c4 r2r4 colored">Three</div>
        </div>
 

 */

class MyGrid extends React.Component {
    constructor (props) {
        super(props);
    }

    render () {
        let gridElem1 = React.createElement(                                     
            "div", {class: this.props.elem_class}, "one");

        let gridMain = React.createElement(
            "div", {class: this.props.grid_class}, gridElem1);

        return (
            gridMain
        )
    }
}

let grid_props = {
    elem_class: "gelem c1c4 r1r2 colored",
    grid_class: "grid-layout-1 c3"
};

let gridElem = React.createElement(MyGrid, 
    grid_props, 
    null)
ReactDOM.render(gridElem, document.getElementById('grid'));


class MyForm extends React.Component {
    constructor (props) {
        super(props);
        this.state = { name: ''};
    }
 
    myChangeHandler = (event, value) => {
        console.log(value);
        this.setState({name: event.target.value});
    }

    submitForm = (event, value) => {
        alert("Submitted")
        console.log(value);
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
        let elem_submit = React.createElement(
            "button", {onClick: this.submitForm}, "Submit");

        let elem_form = React.createElement(
            "form", null, elem_header, elem_para, elem_input, elem_submit);
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
