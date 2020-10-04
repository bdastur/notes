#!/bin/bash
echo "Prometheus Start script"

echo "$@"

#./start.sh --config.file /etc/prometheus/prometheus.yml --storage.tsdb.path /prometheus_data/ --web.console.libraries /etc/prometheus/console_libraries/ --web.console.templates /etc/prometheus/consoles

/usr/local/bin/prometheus $@

