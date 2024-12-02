#!/usr/bin/env python

import sys
from kubernetes import client, config, watch

config.load_kube_config()

v1 = client.CoreV1Api()

api_instance = client.AdmissionregistrationApi()

try:
      api_response = api_instance.get_api_group()
      print("API response: ", api_response)
except client.rest.ApiException as e:
      print("Exception %s" % e)


# watch on pods in all namespaces.
w = watch.Watch()
for event in w.stream(v1.list_pod_for_all_namespaces):
        print("Event: %s %s %s" % (event['type'],
              event['object'].kind, event['object'].metadata.name))

