# Prometheus.



## Best Practices
* [Prometheus Instrumentation](https://prometheus.io/docs/practices/instrumentation/#counter-vs-gauge-summary-vs-histogram)


### Naming:
* Ascii letters and digits, as well as underscores and colons.
```
[a-zA-Z_:][a-zA-Z0-9_:]*
```

### Using labels.
* When you want to have multiple metrics that you want to add/average/sum, 
  they should usually be one metric with labels rather than multiple metrics.

* Example: Rather than http_response_200_total and http_response_404_total, have
  a single metric http_response_total and label 'code' for HTTP response code.

* As a rule of thumb no part of a metric name shouuld be procedurally generated.
  Use labels instead.

* Labels enable prometheus's dimensional data model: any given combination of
  labels for the same metric name identifies a particular dimensional instantiation
  of that metric. Changing any label value, including adding or removing a label, 
  will create a new time series.

* A label with an empty label value is considered equivalent to a label that 
  does not exist.
