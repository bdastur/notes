
# Building the android builder image
```
docker build --tag bdastur/android_builder:latest --platform linux/x86_64 .
```

# Running the container:
```
docker run --platform linux/x86_64 -it bdastur/android_builder /bin/bash 
```
