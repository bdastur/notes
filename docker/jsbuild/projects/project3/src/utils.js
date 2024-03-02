import { DynamoDBClient, ListTablesCommand } from "@aws-sdk/client-dynamodb";


export function getAWSCredentials() {
    return({
      accessKeyId: "ASxxxxNT",
      secretAccessKey: "8xxxxx"
      sessionToken: "IQoJxxxx"
    });
}

export async function ListAsyncBuckets(region) {
    let data = {}
    console.log("Invoked ListAsyncBuckets");
    try {
        const client = new DynamoDBClient({
            region: region,
            credentials: getAWSCredentials()
        });
        command = new ListTablesCommand({});
        data = await client.send(command);
        console.log("data in list bucket: " + JSON.stringify(data));
        return(data);
    } catch (err) {
        console.error(err);
        return data;
    } finally {
        console.log("In finally!");
    }
    return(data);
}

export function ListBuckets() {
    let data = {};
    const listBuckets = async() => {
        try {
            const client = new DynamoDBClient({
                region: "us-east-1",
                credentials: getAWSCredentials()
            });
            command = new ListTablesCommand({});
            data = await client.send(command);
	    console.log("data in list bucket: " + JSON.stringify(data));
	    return(data);
        } catch (err) {
            console.error(err);
    	    return data;
        } finally {
            console.log("In finally!");
        }
    }
    data = listBuckets();
    return(data);
}
