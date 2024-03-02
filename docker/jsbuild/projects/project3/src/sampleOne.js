/* React Imports */
import { createRoot } from "react-dom/client";
import { useState, useEffect, createContext } from 'react';
import React from 'react';


/*
 * An example of a sibling propogating message to parent and other sibling.
 * Message is propogated from child to parent to other siblings.
 * 1. Parent defines a function, in this case updateMessageFromSiblingOne and
 *    passes that as props to the child (siblingOne)
 * 2. Sibling two has an event handler that invokes the callback function from
 *    the event handler with updated message.
 */

const MessageContext = createContext({
    contextMessage: "Initial message",
    updateContextMessage: () => {},
});

function MessageProvider({ children }) {
    const [message, setMessage] = useState("Initial message");

    const updateMessage = (newMessage) => {
       setMessage(newMessage); 
    }
    return (
        <MessageContext.Provider value={{ message, updateMessage }}>
            {children}
        </MessageContext.Provider>
    );
}


function SiblingOne({ person, size, updateMessage }) {
    const [clickCount, setClickCount] = useState(0);

    console.log("Prop person: " + person + size);

    const handleClick = () => {
        setClickCount(clickCount + 1);
        updateMessage("Handled click from sibling one: " + clickCount);
    }
    return(
        <div>
            <h2>Sibling {person.name} size: {size}</h2>
            <button onClick={handleClick}>Update button</button>
        </div>
    );
}

function SiblingTwo({message}) {
    return(
        <h2>Sibling Two. This is the message I got: {message} </h2>
    );
}

function MainApp() {
    const [message, setMessage] = useState("Initial message");

    const updateMessageFromSiblingOne = (newMessage) => {
        setMessage(newMessage);
    }

    return(
        <div>
            <h1>Welcome to SampleOne App</h1>
            <SiblingOne 
             person={{ name: "Jacobson", imageId: "xyz" }}
             size={10}
             updateMessage={updateMessageFromSiblingOne}/>
            <SiblingTwo message={message} />
            <h3>(Parent) Message from sibling one: {message} </h3>
        </div>
    );
}



const container = document.getElementById("app");
const root = createRoot(container);
root.render(<MainApp />);

