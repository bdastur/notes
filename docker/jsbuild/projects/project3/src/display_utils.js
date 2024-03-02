/* React Imports */                                                                  
import { createRoot } from "react-dom/client";                                       
import { useState, useEffect, createContext } from 'react';                          
import React from 'react';    



export function displayListElements(inputList) {
    return(
        <div className="flex p-6">                                                                           
            <ul className="list-none hover:list-disc">                                                                     
            {inputList.map((elem) => (                                                 
                <li key={elem} className="font-sans hover:font-serif text-orange-900">{elem}</li>                                         
            ))}                                                                      
            </ul>                                                                    
        </div>  
    );
}
