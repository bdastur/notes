# wrk:

[wrk - a HTTP benchmarking tool](https://github.com/wg/wrk)


## Building

```
docker build --tag=bdastur/wrk:0.1 .
```


## Running

``` 
sudo docker run --net=host bdastur/wrk:0.1 wrk  --threads 40 --connections 250 --duration 50s --latency http://localhost:9090/graph
```
