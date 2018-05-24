package main

/*
 * Example of a simple http server.
 */

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

/*
 * The message struct represents the json
 * request body, that the client will send.
 */
type Message struct {
	Id   int64  `json:"id"`
	Name string `json:"name"`
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	message := r.URL.Path
	fmt.Println("URL Path: ", message)
	fmt.Println("Request: ", r)

	b, err := ioutil.ReadAll(r.Body)

	fmt.Println("Request body: ", b)

	defer r.Body.Close()
	if err != nil {
		http.Error(w, err.Error(), 500)
		return
	}

	// Unmarshal
	var msg Message
	err = json.Unmarshal(b, &msg)
	if err != nil {
		http.Error(w, err.Error(), 500)
		return
	}

	output, err := json.Marshal(msg)
	if err != nil {
		http.Error(w, err.Error(), 500)
		return
	}
	fmt.Println("Output: ", output)
	w.Header().Set("content-type", "application/json")

	w.Write(output)
	//w.Write([]byte(message))
}

func main() {
	fmt.Println("A Simple Server!")
	http.HandleFunc("/", indexHandler)
	if err := http.ListenAndServe(":8080", nil); err != nil {
		panic(err)
	}

}
