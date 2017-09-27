# Java, Maven


## Maven 5 min setup guide.
The steps detailed here are to setup the most minimal maven project from
start to finish.

1. Download Maven.
```
> curl http://mirrors.ibiblio.org/apache/maven/maven-3/3.5.0/binaries/apache-maven-3.5.0-bin.tar.gz \
-o apache-maven-3.5.0-bin.tar.gz

tar -xvzf apache-maven-3.5.0-bin.tar.gz
```

2. Set mvn binary to your $PATH
```
export PATH="$PATH:/home/brd/CODE/synthetic/javac/apache-maven-3.5.0/bin/"
```

3. Generate a project template with archetype:Generate
```
> mvn archetype:generate \
  -DgroupId=com.mycompany.app \
  -DartifactId=my-app \
  -DarchetypeArtifactId=maven-archetype-quickstart \
  -DinteractiveMode=false

```

4. Mvn Build
```
> cd my-app
> mvn package

```

5. Run.
To run the compiled code.

```
java -cp target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App

```

## Maven useful links:

* Maven getting started:
  https://maven.apache.org/guides/getting-started/index.html

* POM file details:
  https://maven.apache.org/ref/3.5.0/maven-model/maven.html
