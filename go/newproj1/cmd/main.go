package cmd

import (
        "fmt"
        "os"
        "github.com/spf13/cobra"
)

// ClusterName Name of the cluster where the node needs to be added
var ClusterName string


func NewCmdAddNodePool() *cobra.Command {
    cmd := &cobra.Command{
                Use:   "add-nodepool (-f | --filename)",
                Short: "Add a new Nodepool.",
                Run: func(cmd *cobra.Command, args []string) {
                    fmt.Println("Run cobra command")
                },
    }

    cmd.Flags().StringVarP(&ClusterName, "clustername", "", "", "The cluster where the operation needs to be performed")

    return cmd
}

// NewILMCommand Initialization of all the commands
func NewProjCommand() *cobra.Command {
        cmd := &cobra.Command{
                Use:   "newproj",
                Short: "A new project command",
                Long:  ``,
                Run:   runHelp,
        }

        cmd.AddCommand(NewCmdAddNodePool())
        return cmd
}

func runHelp(cmd *cobra.Command, args []string) {
    if err := cmd.Help(); err != nil {
        os.Exit(1)
    }
}

