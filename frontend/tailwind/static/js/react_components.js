class Button extends React.Component {
    constructor (props) {
        super(props);
    }

    render () {
        let gridElement1 = React.createElement(
            "div", {class: this.props.elem_class}, "one");

        let gridMain = React.createElement(
            "div", {class: this.props.grid_class}, gridElement1);
        
        return (gridMain);
    }
}

let grid_props = {
    elem_class: "block bg-blue-100 p-2 border border-1 border-blue-500 text-center",
    grid_class: "flex block border border-1 border-blue-500"
}

let gridElement = React.createElement(Button, grid_props, null);
ReactDOM.render(gridElement, document.getElementById("rgrid"));