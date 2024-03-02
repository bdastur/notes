/* React Imports */
import { createRoot } from "react-dom/client";
import { useState, useEffect } from 'react';
import React from 'react';

/* AWS SDK Imports */
import { DynamoDBClient, ListTablesCommand } from "@aws-sdk/client-dynamodb";

/* MaterialUI Imports */
import Button from '@mui/material/Button';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

/* Local imports */
import { getAWSCredentials } from "./utils";


/*
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    console.log("App handleClick!");
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Welcome to my app</h1>
    </div>
  );
}
*/

/*
 * Props: {
 *  'credentials': AWS Credentials (Access key, secret, token)
 *  'operation': Name of the operation List/Get/Update etc.
 */

function callDDB(region, credentials) {
    console.log("DDBcall: " + region + " :: " + credentials);
    let response = {};
    let awsCall = async () => { 
    try {
        let ddbClient = new DynamoDBClient({
            region: region, 
            credentials: credentials
         });
         let command = new ListTablesCommand({});
         response = await ddbClient.send(command);
	 console.log("HEre 1 Response: " + JSON.stringify(response));
     } catch (err) {
         console.log(err);
     } finally {
         console.log("in finally");
     }
    }
    awsCall();

    console.log("BRD: here 444: " + JSON.stringify(response));
    return response;
}

class DynamoDBListTablesClass extends React.Component {
    constructor (props) {
      super(props);
      this.state = {"tables": [],
	            "isLoading": false 
                   };
    }

    displayTable(tables) {
	console.log("Display table: " + tables);
        return(
            <TableContainer component={Paper}>
                <Table width="500px" aria-label="simple table">
                  <TableHead>
                    <TableRow>
                        <TableCell>DynamoDB Table Name</TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                      {tables.map((table) => (
                          <TableRow>
                              <TableCell>{table}</TableCell>
                          </TableRow>
                       ))}
                  </TableBody>
                </Table>
            </TableContainer>
        );
    }


    componentDidMount() {
        console.log("DynamodbListTables component did mount: " + JSON.stringify(this.props)); 

	/*
	let awsCall = async () => {
	    try {
	        let ddbClient = new DynamoDBClient({
                    region: this.props.region,
        	    credentials: this.props.credentials
	        });
	        let command = new ListTablesCommand({});
	        let response = await ddbClient.send(command);
                console.log(response);
		this.setState({tables: response["TableNames"]});
	    } catch (err) {
	        console.log(err);
	    } finally {
                console.log("in finally");
	    }  
	});
        awsCall();
	*/ 
        let response = callDDB(this.props.region, this.props.credentials);
	console.log("In component did mount response: " + JSON.stringify(response));
        this.setState({'tables': response["TableNames"]});
    }

    render() {
	console.log("Dynamodb props: " + JSON.stringify(this.props));
	console.log("My State: " + JSON.stringify(this.state)); 

        return(
		this.displayTable(this.state["tables"])
	);
    }
}

function DynamoDBListTables(props) {
    let [tables, setTables] = useState([]);
    console.log("Arguments/Props: " + JSON.stringify(props));

    function displayText() {
        return <h1>DynamoDB List Tables {tables}</h1>;
    }

    function displayTable(data) {
        return(
	    <TableContainer component={Paper}>
		<Table width="500px" aria-label="simple table">
                  <TableHead>
                    <TableRow>
                        <TableCell>DynamoDB Table Name</TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
	  	      {tables.map((table) => (
			  <TableRow>
		              <TableCell>{table}</TableCell>
			  </TableRow>
                       ))}
                  </TableBody>
                </Table>
            </TableContainer>
	);
    }

    useEffect(() => {
        console.log("Use effect");
	const listTables = async() => {
            console.log("Async list buckets");
	    try {
	        let ddbClient = new DynamoDBClient({
			region: props.region,
			credentials: props.credentials
		});
		let command = new ListTablesCommand({});
		let response = await ddbClient.send(command);
                console.log(response.TableNames);

		setTables(response.TableNames);
		console.log("state: " + tables);
	    } catch (err) {
                console.log(err);
	    } finally {
                console.log("In Finally");
	    }
	}
        listTables();
	console.log("Tables: " + tables);

    }, []);

    return(
        displayTable(tables)

    );
}


class MainApp extends React.Component {
    constructor (props) {
      super(props);
    }

    render () {
      let credentials = getAWSCredentials();

      let operation = "ListTables";
      let outputType = "Table";
      return (
      <div>
        <h1>Welcome to the Main App</h1>
	<DynamoDBListTablesClass region="us-east-1" credentials={credentials} outputType={outputType}  />
      </div>
      );
    }
}


const container = document.getElementById("app");
const root = createRoot(container);
root.render(<MainApp />);

