package tfrenderer

import (
	"fmt"
	"io/ioutil"
	"os"
	"text/template"
)

type Inventory struct {
	Material string
	Count    uint
}

// Multiline string should have back tics
var template_data = ` 
{{ .Count}} items are made of {{.Material}}
`

func RenderTemplate() {
	sweaters := Inventory{"wool", 32}
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
	dat, err := ioutil.ReadFile(template_file)
	check(err, "Failed to read file")
	fmt.Print(string(dat))

}
