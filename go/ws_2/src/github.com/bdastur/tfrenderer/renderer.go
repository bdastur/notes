package tfrenderer

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"text/template"

	"gopkg.in/yaml.v2"
)

type Inventory struct {
	Material string
	Count    uint
    Properties []Property
}

type Property struct {
    Cost   int
    Vendor string
}

// Multiline string should have back tics
var template_data = ` 
{{ .Count}} items are made of {{.Material}}
`

func NewProperty(cost int, name string) Property{
    property := Property{cost, name}
    return property
}

func RenderTemplate() {
	fmt.Println("RenderTemplate Start")
    pp := NewProperty(43, "zyx corp")

    var sweaters Inventory
    sweaters.Material = "Wool"
    sweaters.Count = 43
    sweaters.Properties = append(sweaters.Properties, pp)

	//sweaters := Inventory{"wool", 32, [3, "Xyz corp"]}
	tmpl, err := template.New("test1").Parse(template_data)
	if err != nil {
		panic(err)
	}
	err = tmpl.Execute(os.Stdout, sweaters)
	if err != nil {
		panic(err)
	}
}

func check(e error, msg string) {
	if e != nil {
		fmt.Println(msg)
		panic(e)
	}
}

func RenderTemplateFromFile(template_file string) {
	fmt.Println("Render Template from File")
	dat, err := ioutil.ReadFile(template_file)
	check(err, "Failed to read file")
	fmt.Print(string(dat))
	template_data := string(dat[:])

	// Now parse this data.
    pp := NewProperty(23, "zyx corp")
    var sweaters Inventory
    sweaters.Material = "Wool"
    sweaters.Count = 43
    sweaters.Properties = append(sweaters.Properties, pp)

    pp = NewProperty(423, "ABC corp")
    sweaters.Properties = append(sweaters.Properties, pp)

    pp = NewProperty(123, "Cigna corp")
    sweaters.Properties = append(sweaters.Properties, pp)

    pp = NewProperty(233, "Acme corp")
    sweaters.Properties = append(sweaters.Properties, pp)


	//sweaters := Inventory{"wool", 43}

	tmpl, err := template.New("test").Parse(template_data)
	if err != nil {
		panic(err)
	}

	err = tmpl.Execute(os.Stdout, sweaters)
	if err != nil {
		panic(err)
	}

}

var jsonstring = ` 
{
	"cluster_name": "brdtest",
	"service_name": "testservice"
}
`

type environment struct {
	ClusterName string `json:"cluster_name"`
	ServiceName string `json:"service_name"`
}

func ParseJsonData() {
	fmt.Println("ParseJsonData, jsonstring: ", jsonstring)
	env := environment{}

	jsonbytes := []byte(jsonstring)
	fmt.Println("jsonbytes: ", jsonbytes)
	json.Unmarshal(jsonbytes, &env)
	fmt.Println("Env: ", env.ClusterName)
}

type configuration struct {
	ClusterName string `yaml:"cluster_name"`
	ServiceName string `yaml:"service_name"`
}

func ParseYamlDataFile(config_file string) {
	fmt.Println("ParseYamlData")
	yamlFile, err := ioutil.ReadFile(config_file)
	check(err, "Could not read YAML file")

	configVar := configuration{}
	err = yaml.Unmarshal(yamlFile, &configVar)
	fmt.Println("Config: ", "cluster name: ",
		configVar.ClusterName, "Service: ", configVar.ServiceName)

}
