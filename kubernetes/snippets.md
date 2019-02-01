## Printing the last time all containers in a pod terminated

```
kc get pods -o json \
    -n kube-system -l "k8s-app=canal" | jq -r '.items[]|{"pod":.metadata.name,"container":[{"name":.status.containerStatuses[].name,"last_terminated":.status.containerStatuses[].lastState.terminated.finishedAt}]}'
```

## Get the reequest memory for every container in every pod:
```
kubectl get pods \
  --all-namespaces \
  -o=jsonpath="{range .items[*]}{.metadata.namespace}:{.metadata.name}{'\n'}{range .spec.containers[*]}  {.name}:{.resources.requests.memory}{'\n'}{end}{'\n'}{end}"
```
