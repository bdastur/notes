package main

import (
	"flag"
	"fmt"
	"os"

	"github.com/bdastur/aws"
	"github.com/bdastur/datatypes"
	"github.com/bdastur/tfrenderer"
)

func build_cli(args []string) {
	// Using Printf function
	//fmt.Printf("os arguments: %s %s", args, "\n")
	fmt.Println("Arguments: ", args)

	/*
	 * Note: When using flags. The falgs should always be provided
	 * first before any arguments.
	 * Example $ ./bin/examples -dry-run=true <arg1> <arg2>
	 */
	// Get options (flags)
	wordPtr := flag.String("word", "default-word", "A random string")
	numPtr := flag.Int("count", 10, "A random number")
	boolPtr := flag.Bool("dry-run", true, "Boolean flag true/false")

	flag.Parse()

	fmt.Println("WordPtr: ", *wordPtr)
	fmt.Println("numPtr: ", *numPtr)
	fmt.Println("Bool ptr: ", *boolPtr)
	fmt.Println("Arguments: ", flag.Args())
}

func usage() {
	usageMessage := "Usage: " + "\n" +
		"./bin/examples <operation>" + "\n" +
		"operations: " + "\n" +
		"  testcmd" + "\n" +
		"  string" + "\n" +
		"  datatypes" + "\n" +
		"  templates" + "\n" +
		"  json" + "\n" +
		"  yaml" + "\n" +
		"  aws" + "\n"

	fmt.Println(usageMessage)
}

func Reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

func reverseString(str []string) []string {
	var reverseStr []string
	fmt.Println("String to reverse: ", str, "Len: ", len(str))
	for i := 0; i < len(str)-1; i = i + 1 {
		fmt.Println("str: ", str[i])
	}

	for i := len(str) - 1; i >= 0; i = i - 1 {
		rstr := Reverse(str[i])
		reverseStr = append(reverseStr, rstr)
		fmt.Println("str:: ", str[i])
	}
	return reverseStr
}

func build_nested_cli(args []string) {
	// Validate cmd line arguments.
	if len(args) <= 1 {
		fmt.Printf("Arguments not provided")
		usage()
		os.Exit(1)
	}
	// Operation: testcmd
	testOperation := flag.NewFlagSet("testcmd", flag.ExitOnError)
	messageOption := testOperation.String("message", "Test Message",
		"A random String")

	// Operation: string concatenation.
	strOperation := flag.NewFlagSet("string", flag.ExitOnError)
	reverseOption := strOperation.Bool("reverse", false,
		"Whether to reverse string")

	// Datatypes.
	datatypesOperation := flag.NewFlagSet("datatypes", flag.ExitOnError)
	integerOption := datatypesOperation.Bool("integer", true, "Integer test")
	vdOption := datatypesOperation.Bool("declaration", true,
		"Variable Declaration")

	//Operation: templates
	templatesOperation := flag.NewFlagSet("templates", flag.ExitOnError)
	templateOption := templatesOperation.String("filename", "",
		"Filename")

	// Operation: json
	jsonOperation := flag.NewFlagSet("json", flag.ExitOnError)
	jsonOption := jsonOperation.String("jsonfile", "", "Json Filename")

	// Operation: yaml
	yamlOperation := flag.NewFlagSet("yaml", flag.ExitOnError)
	yamlOption := yamlOperation.String("configfile", "", "Yaml config file")

	// Operation: aws
	awsOperation := flag.NewFlagSet("aws", flag.ExitOnError)

	//Composite types.
	compositesOperation := flag.NewFlagSet("composites", flag.ExitOnError)

	switch args[1] {
	case "testcmd":
		testOperation.Parse(args[2:])
	case "string":
		strOperation.Parse(args[2:])
	case "datatypes":
		datatypesOperation.Parse(args[2:])
	case "composites":
		compositesOperation.Parse(args[2:])
	case "templates":
		templatesOperation.Parse(args[2:])
	case "json":
		jsonOperation.Parse(args[2:])
	case "yaml":
		yamlOperation.Parse(args[2:])
	case "aws":
		awsOperation.Parse(args[2:])
	default:
		fmt.Printf("%q is not a valid command. \n", args[1])
		os.Exit(2)
	}

	if testOperation.Parsed() {
		if *messageOption == "" {
			fmt.Printf("Option cannot be blank")
		} else {
			fmt.Printf("Message option: %s ", *messageOption)
		}
	} else if strOperation.Parsed() {
		if *reverseOption == true {
			fmt.Printf("Reverse option set. \n")
			fmt.Println("Arguments: ", strOperation.Args())
			rstr := reverseString(strOperation.Args())
			fmt.Println("Reverse String: ", rstr)
		} else {
			fmt.Printf("Reverse option is false")
		}
	} else if datatypesOperation.Parsed() {
		if *vdOption == true {
			datatypes.VariableDeclaration()
		}
		if *integerOption == true {
			fmt.Println("Integer datatype")
			datatypes.IntegerDatatype()
		}
		datatypes.IntegerDatatype()
	} else if compositesOperation.Parsed() {
		fmt.Println("Test composites")
		datatypes.CompositeTypes()
	} else if templatesOperation.Parsed() {
		fmt.Println("Render file: ", *templateOption)
		if *templateOption == "" {
			tfrenderer.RenderTemplate()
		} else {
			tfrenderer.RenderTemplateFromFile(*templateOption)
		}
	} else if jsonOperation.Parsed() {
		fmt.Println("Parsed json operation")
		if *jsonOption == "" {
			tfrenderer.ParseJsonData()
		}
	} else if yamlOperation.Parsed() {
		fmt.Println("Parse yaml file")
		if *yamlOption == "" {
			fmt.Println("Require a yaml file!")
		} else {
			tfrenderer.ParseYamlDataFile(*yamlOption)
		}
	} else if awsOperation.Parsed() {
		fmt.Println("AWS: ", args[2:])
		switch args[2] {
		case "s3":
			fmt.Println("S3 operation")
			listOperation := flag.NewFlagSet("list", flag.ExitOnError)
			listOption := listOperation.Bool("all", false, "List all buckets")
			awsroleOption := listOperation.String("role", "", "Role ARN")
			awsbucketnameOption := listOperation.String("bucketname", "", "Bucket name")
			switch args[3] {
			case "list":
				fmt.Println("List operation: ")
				listOperation.Parse(args[4:])

			default:
				fmt.Println("Default")
			}

			if listOperation.Parsed() {
				fmt.Println("Aws operation list ", args[1:])
				fmt.Println("List option: ", *listOption)
				aws.ListBuckets(*awsroleOption, *awsbucketnameOption)

			}
		}

	}

}

func main() {
	fmt.Println("Examples !")

	//build_cli(os.Args)
	build_nested_cli(os.Args)

}
