## Printing the last time all containers in a pod terminated

```
kc get pods -o json \
    -n kube-system -l "k8s-app=canal" | jq -r '.items[]|{"pod":.metadata.name,"container":[{"name":.status.containerStatuses[].name,"last_terminated":.status.containerStatuses[].lastState.terminated.finishedAt}]}'
```

## Get the request memory for every container in every pod:
```
kubectl get pods \
  --all-namespaces \
  -o=jsonpath="{range .items[*]}{.metadata.namespace}:{.metadata.name}{'\n'}{range .spec.containers[*]}  {.name}:{.resources.requests.memory}{'\n'}{end}{'\n'}{end}"
```


## Get volume id for a PVC attached to a POD:
```
kubectl get pods dummy-0 -o jsonpath="{.metadata.name}: {range .spec.volumes[*]}  {.persistentVolumeClaim} {'\n'}{end}" | grep claimName
kubectl get pvc dummyvol-dum-0 -o jsonpath="{.spec.volumeName} {'\n'}"
kubectl get pv pvc-axxxxe5e-0xxxx22184c7e3d4  -o jsonpath="{.spec.awsElasticBlockStore.volumeID} {'\n'}"

```

## test.
```
kubectl get pods esbi-0 -o jsonpath="{.metadata.name}: {.apiVersion} {.metadata.namespace}{range .spec.containers[*]} {.name} {'\n'} {range .volumeMounts[*]} {end} {end} {'\n'}"

```

## Get kube events sorted by timestamp

```
kubectl get event --sort-by='.metadata.creationTimestamp'
```
