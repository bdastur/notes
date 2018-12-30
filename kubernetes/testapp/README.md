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





