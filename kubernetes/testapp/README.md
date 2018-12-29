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
