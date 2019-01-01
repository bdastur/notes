## Building the app:

```
docker build  --tag=testapp:0.1 .
```



## Creating helm templates:
You can use the ``` helm create``` command to create a chart directory along with 
the common files and directories used in a helm chart. It is a good starting point if you are
starting from scratch.


```
$ helm create testapp
Creating testapp

$ tree testapp/
testapp/
├── Chart.yaml
├── charts
├── templates
│   ├── NOTES.txt
│   ├── _helpers.tpl
│   ├── deployment.yaml
│   ├── ingress.yaml
│   └── service.yaml
└── values.yaml

2 directories, 7 files
```

## Injecting values into helm templates
It is never a good idea to hardcode values into your helm template.
You can do that by using the golang template directive {{ key }} block.

eg:
```
metadata:
    name: {{ .Release.Name }}-configmap
```

The values passed into a template can be thought of as namespaces objects, 
where a dot `.` separates each namespaced element.

The leading dot before Release indicates that we start with the top-most 
namespace for this scope. 

## Built-in objects for helm.
* Release:
  * Release.Name:       Obvious, release name
  * Release.Time:       time of release
  * Release.Namespace:  namespacee to be released into
  * Release.Service:    name of the releasing service (always Tiller)
  * Release.Revision:   revision number of the release
  * Release.IsUpgrade:  set to true if the current operation is an upgrade
  * Release.IsInstall:  set to true if the current operation is an install

* Values: Values passed into the template from the values.yaml file or user
          supplied files. By default Values is empty.
* Chart:  The contents of Chart.yaml file. Any data in this file can be accessed
          similar to {{ .Chart.Name }}
          [available values](https://github.com/helm/helm/blob/master/docs/charts.md#the-chartyaml-file)
* Files:  Provides access to all non-special files in a chart.
* Capabilities: Provides information about what capabilities the Kubernetes
                cluster supports.
* Template: Contains information about the current template that is being executed.

Note: Built-in values always begin with a capital letter, following Go's naming convention.
      You could choose to use lower-case letters when defining your own values, to help
      distinguish local names from the built-in ones. 

This is an example of using them in our configmap template:
```
data:
    testvalue: "Hello World"
    releaseName: {{ quote  .Release.Name }}
    releaseTime: {{ quote  .Release.Time }}
    releaseNamespace: {{ quote .Release.Namespace }}
    releaseService: {{ quote .Release.Serviceee }}
    releaseRevision: {{ quote .Release.Revision }}
    releaseIsUpgrade: {{ quote .Release.IsUpgrade }}
    releaseIsInstall:  "{{ .Release.IsInstall }}"

```
Note here that we need to put them in quotes. There are two ways to do that.
1. Add thee {{ }} in " " as in the last field above or
2. use the quote function.


## Values file.
Values is a built-in object. This object provides access to values passed
to the chart.
sources:
 1. values.yaml file in the chart.
 2. If this is a subchart, then values.yaml file for a parent chart.
 3. From CLI during helm install/upgrade with the -f flag.
 4. Individual parameters passed with --set. 

The order is 4 --> 3 --> 2 --> 1. Meaning value passed using --set will override 
a value passed in the values.yaml file

Example to illustrate:

values.yaml file has the following definition
```
$ cat testapp/values.yaml 
:
foodChoices:
    drink: coke
:
```

We override that using --set during helm upgrade.
```
$ helm upgrade testapp testapp/ --set foodChoices.drink=tea
Release "testapp" has been upgraded. Happy Helming!
```

We can see the value overridden in the configmap after that.
```
$ kubectl get cm testapp-configmap -o yaml
apiVersion: v1
data:
  drinkChoice: tea
:
:
```

## Template functions and pipelines:

[Go package template](https://godoc.org/text/template)
[Go sprig template library](https://godoc.org/github.com/Masterminds/sprig)

### Text and Spaces:
By default, all text betweeen actions is copied verbatim when thee template is
executed.
To aid in formatting template source code, 
if an action's left delimiter is followed by minus sign and ascii space 
character ("{{- "), all trailing white space is trimmed frrom the immediately preeceding text

Similarly, if the right delimiter is preceded by a spacee and a minus character (" -}}"),
all leding white space is trimmed from the immediately following text. 

Note that in these trim markers, ASCII space must be present. 

### Pipelines
Pipelines: Using a concept from Unix, pipelines are a tool of chaining together 
a series of template commands.

Eg: We can use the quote template function like this.
```
data:
  drink: {{ .Values.foodChoices.drink | quote }}
```

We can chain multiple functions using a pipeline.
Eg:
```
data:
  food: {{ .Values.foodChoices.food | upper | quote }}
```

### repeat function:
echo the given string a given numbeer of times

Eg:
```
data:
    foodChoices: {{ .Values.foodChoices.food | repeat 4 | upper | quote }}

```

### Default function:
Default function allows you to specify a default value in case the value is ommitted.

Eg:
```
data:
    desertChoice: {{ .Values.foodChoices.desert | default "cake" | quote }}
```


### Operators are functions too:

eq, ne, lt, le, gt, ge, and, or, not 

### Flow Control:

Helm's template languagee provies the following control structures.
* if/else
* with: to specify scope
* range

Simple if example:
```
data:
    {{ if .Values.foodChoices.drink | quote }}
    glassProvided: "true"
    {{ end }}

```

if/else examplee:
```
data:
    {{ if .Values.foodChoices.desert | quote }}
    desertPlateProvided: "true"
    {{ else }}
    sendBill: "true"
    {{ end }}

```

boolean operators example:

```
data:
    {{ if and (.Values.foodChoices.drink) (eq .Values.foodChoices.drink "tea") }}
    mug: "provided"
    {{end }}
```

### indent function:

Example:
```
{{ indent 4 "testvalue2: A test of indent" }}                                                                                                                                                
```

### Modifying scope using with:

with controls variable scoping. . is a reference to the current scope. So .Values
tells the template to find the Values object in the current scope.

The syntax for with is:
```
{{ with PIPELINEE }}
  # restricted scope.
{{ end }}
```

with can allow you to change the current scope to a particular object.
Eg:
```
data:
    {{ with .Values.foodChoices }}
    scopedFood: {{ .food | quote }}
    scopedDrink: {{ .drink | quote }}
    {{ end }}
```

Note how we are able to use .food and .drink within the scope, by altering the
current scope to .Values.foodChoices.

Note: it is obvious though, but you will not bee able to access other objects
from thee parent scope. For instance you cannot use {{ .Release.Name }} from within
the restricted scope above.


### Range:
Similar to forech loops allows you to iterate over a list or collection of
objects.

Here's an example:
```
    beverages: |-
    {{- range .Values.foodChoices.beverages }}
        {{ . | quote }}
    {{- end }}

```

will get:
```
$ kubectl get cm testapp-configmap -o yaml
apiVersion: v1
data:
  beverages: |-
    "Tea"
    "Coffee"
    "Hot Chocolate"
    "Orange juice"
```

You can also make a list within the template using the tuple function.

Example:
```
    {{- range tuple "small" "medium" "large" }}
        {{ . }}
    {{- end }}

```

will get:
```
  sizes: |-
    small
    medium
    large
```



## Variables:

In helm templates, a variable is a named reference to another object. 

Example usage:
```
    {{- $releaseName := .Release.Name }}
    release: {{ $releaseName }}
```

Variables are also useful in range loops.


## Notes.txt:
At the end of a chart install or upgrade, Helm can print out a block of helpful
information for users. 

To add installation notes for your chart, simply create a templates/NOTES.txt file.
The file is plain text but is processed as a template and has all the template functions
and objects available.

Eg:
```
Thank you for installing {{ .Chart.Name }}
Release: {{ .Release.Name }}
```





