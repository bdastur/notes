/*
 * Notes: 
 * - React components must start with a capital letter,
 *   while HTML tags must be lowercase. That's how you know its a
 *   React component
 * - JSX is stricter than HTML. You have to close tags like <br />. Your component also
 *   cannot return multiple JSX tags. You have to wrap them in a shared parent, like
 *   a <div>...</div> or an empty <>...</> wrapper.
 */
import { createRoot } from "react-dom/client";
import { useState } from 'react';

const user = {
  name: "Dan Johnson",
  age: 54
};

const products = [
  { name: "Cabbage", isFruit: false, id: 1},
  { name: "Eggplan", isFruit: false, id: 2},
  { name: "Mango", isFruit: true, id: 3},
]

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    alert("You clicked me");
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
	  Clicked {count} times
    </button>
  )
}

function About() {
  return (
    <>
      <h1>About</h1>
      <p>Hello there {user.name }. <br/>How do you do? Are you {user.age} years old now?</p>
    </>
  )
}

function ProductList() {
  const listItems = products.map(product =>
    <li
      key={product.id}
      style={{
        color: product.isFruit ? 'magenta' : 'darkgreen'
      }}
    >
      {product.name}
    </li>
  );

  return (
    <ul>{listItems}</ul>
  );

}

export default function MyApp() {
    return (
      <div>
	    <h1 className="colored">Welcome to my app</h1>
	    <MyButton />
	    <About />
	    <ProductList />
      </div>
    );
}


const container = document.getElementById("app");
const root = createRoot(container);
root.render(<MyApp />);

