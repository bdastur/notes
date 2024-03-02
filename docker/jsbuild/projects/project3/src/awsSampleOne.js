/* React Imports */
import { createRoot } from "react-dom/client";
import { useState, useEffect, createContext } from 'react';
import React from 'react';

/* Local imports */
import { getAWSCredentials, ListBuckets, ListAsyncBuckets } from "./utils";
import { displayListElements } from "./display_utils";



function DDBListTablesWidget({region}) {
    const [tables, setTables] = useState([]);
    const [tablesFound, setTablesFound] = useState(false);
    const [inputValue, setInputValue] = useState("");


    useEffect(() => {
        console.log("DDBTablesWidget useEffect");
    });

    const handleClick = () => {
        console.log("Button Clicked!");
        if (!inputValue) {
            console.log("Do nothing, inputValue is empty");
            return;
        }
        const awsCall = async() => {
            data = await ListAsyncBuckets(inputValue);
            setTables(data.TableNames);
            setTablesFound(true);
            console.log("Data: " + JSON.stringify(data));
        }
        console.log("Now should call awsCall");
        awsCall();
    }

    const handleChange = (event) => {
        console.log("Handle change!");
        setInputValue(event.target.value);
        console.log("Change: " + event.target.value);
    }

    if (tablesFound == false) {
        return(
            <div className="flex m-4">
                <label htmlFor="regionInput">Enter Region:</label>
                <input type="text" id="regionInput" 
                 value={inputValue} 
                 onChange={handleChange} />

                <h5>List Tables: {inputValue} </h5>
                <button onClick={handleClick}>List Tables Btn</button>                       
                <h4>List of tables</h4>                                                  
            </div>
        );
    } 
    return (
        displayListElements(tables)
    );
    /*
    return (
        <div>
            {tables.length > 0 && (
                <ul>
                {tables.map((table) => (
                    <li key={table}>{table}</li>
                ))}
               </ul>
            )}
            {tables.length === 0 && !isLoading && <p>No buckets found.</p>}
        </div>
    );
    */
}


function MainApp() {

    return(
        <div className="flex m-4 p4">
            <DDBListTablesWidget region={"us-east-1"} />
        </div>
    );
}



const container = document.getElementById("app");
const root = createRoot(container);
root.render(<MainApp />);

