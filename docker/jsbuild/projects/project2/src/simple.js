/*
 * Notes:
 * - React components must start with a capital letter,
 *   while HTML tags must be lowercase. That's how you know its a
 *   React component
 * - JSX is stricter than HTML. You have to close tags like <br />. Your component also
 *   cannot return multiple JSX tags. You have to wrap them in a shared parent, like
 *   a <div>...</div> or an empty <>...</> wrapper.
 *   Hooks: Functions starting with use are called Hooks. useState is a built-in Hook provided
 *   by React.
 */
import { STSClient, AssumeRoleCommand } from "@aws-sdk/client-sts";
import { ListBucketsCommand, S3Client } from "@aws-sdk/client-s3";
import { DynamoDBClient, ListTablesCommand } from "@aws-sdk/client-dynamodb";
import { createRoot } from "react-dom/client";
import { useState, useEffect } from 'react';
import Button from '@mui/material/Button';

const user = {
  name: "Dan Johnson",
  age: 54
};

const products = [
  { name: "Cabbage", isFruit: false, id: 1},
  { name: "Eggplan", isFruit: false, id: 2},
  { name: "Mango", isFruit: true, id: 3},
]

function getAWSCredentials() {
    return({
      accessKeyId: "xxx",
      secretAccessKey: "xxxx",
      sessionToken: "xxxx.xxx"
    });
}

const ListBuckets = () => {
  const [buckets, setBuckets] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const listBuckets = async () => {
      setIsLoading(true);
      setError(null);
      try{
	console.log("BRD here 1");
	      /*
        const stsClient = new STSClient({
          region: "us-east-1"});

        const command = new AssumeRoleCommand({
          RoleArn: "arn:aws:sts::462972568455:assumed-role/Admin/bdastur-Isengard",
          RoleSessionName: "session1",
          DurationSeconds: 900
        });
        console.log("BRD: here 2");
        const response = await stsClient.send(command);
        console.log("Response from sts: " + response);
	*/
        //S3Client
        const client = new DynamoDBClient({
	  region: "us-east-1",
	  credentials: getAWSCredentials()
	});
	command = new  ListTablesCommand({});
	//command = new ListBucketsCommand({});
        const data = await client.send(command);

        setBuckets(data.TableNames);
	console.log(data);

      } catch (err) {
        console.error(err);
        setError("Failed to list buckets.");
      } finally {
        setIsLoading(false);
      }
    };

    listBuckets();
  }, []);

  return (
    <div>
      {isLoading && <p>Loading buckets...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {buckets.length > 0 && (
        <ul>
          {buckets.map((bucket) => (
            <li key={bucket}>{bucket}</li>
          ))}
        </ul>
      )}
      {buckets.length === 0 && !isLoading && <p>No buckets found.</p>}
    </div>
  );
};


function MuiButton() {
  return <Button variant="contained">Hello MUI</Button>;
}

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
  );
}

function MyButtonWithProps({count, onClick}) {
  return (
    <button onClick={onClick}>
      Button With Props {count}.
    </button>

  );
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
  const [count, setCount] = useState(0);

  function handleClick() {
    console.log("App handleClick!");
    setCount(count + 1);
  }

  return (
    <div>
      <h1 className="colored">Welcome to my app</h1>
      <MuiButton />
      <MyButton />
      <About />
      <ProductList />
      <MyButtonWithProps count={count} onClick={handleClick}/>
      <MyButtonWithProps count={count} onClick={handleClick}/>
      <MuiButton />
      <ListBuckets />
    </div>
  );
}


const container = document.getElementById("app");
const root = createRoot(container);
root.render(<MyApp />);

