package main

import (
	"fmt"
)

type Node struct {
	NodeName string
}

type Cluster struct {
	ClusterName string
	ClusterType string
	Properties  []string
}

func simple_struct() Cluster {
	// Initialize struct.
	var cluster Cluster
	cluster.ClusterName = "Test"
	cluster.ClusterType = "Dev"
	// properties set.
	properties := [3]string{"a", "b"}
	for i := 0; i < len(properties); i++ {
		cluster.Properties = append(cluster.Properties, properties[i])
	}

	// Node
	nodes := [2]Node{{NodeName: "test"}, {NodeName: "test2"}}
	fmt.Println("Nodes: ", nodes)

	return cluster
}

func main() {
	cluster := simple_struct()
	fmt.Println("Cluster is: ", cluster)
}
