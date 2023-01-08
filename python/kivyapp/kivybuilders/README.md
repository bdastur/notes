
# Building the android builder image
```
docker build --tag bdastur/android_builder:latest --platform linux/x86_64 .
```

# Running the container:

```
docker run --user user --platform linux/x86_64 -v $(pwd):/home/user/hostcwd -it bdastur/android_builder /bin/bash 
```
