# Prometheus.



## Best Practices
* [Naming](https://prometheus.io/docs/practices/naming/)
* [Prometheus Instrumentation](https://prometheus.io/docs/practices/instrumentation/#counter-vs-gauge-summary-vs-histogram)


### Naming:
* Ascii letters and digits, as well as underscores and colons.
```
[a-zA-Z_:][a-zA-Z0-9_:]*
```

* Single word. Application prefix relevant to the domain the metric belongs
  to. Sometimes however metrics are more generic, like standardized metrics
  exported by client libraries. Eg:
  - prometheus_notification_total (specific to prometheus)
  - process_cpu_seconds_total  (exported by many client libraries)
  - http_request_duration_seconds  (for all HTTP requests)

* Must have a single unit (dont mix milliseconds or seconds with bytes)
* Should use base units (seconds, bytes, meters not Kilobytes, milliseconds etc)
* Should have a suffix describing the unit in plural form.
* Accumulating count has a suffix total in addition to the unit.


### Using labels.
* When you want to have multiple metrics that you want to add/average/sum,
  they should usually be one metric with labels rather than multiple metrics.

* Example: Rather than http_response_200_total and http_response_404_total, have
  a single metric http_response_total and label 'code' for HTTP response code.

* As a rule of thumb no part of a metric name shouuld be procedurally generated.
  Use labels instead.

* Labels enable prometheus's dimensional data model: any given combination of
  labels for the same metric name identifies a particular dimensional instantiation
  of that metric. **Changing any label value, including adding or removing a label,
  will create a new time series**.

* A label with an empty label value is considered equivalent to a label that
  does not exist.
