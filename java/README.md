# Java, Maven, Gradle


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


## Gradle setup.

1. Download Gradle from the [Gradle releases](https://gradle.org/releases) page.

2. Manually Install Gradle.

```
sudo mkdir /opt/gradle
sudo unzip -d /opt/gradle gradle-8.0.2-bin.zip
Update PATH to include the gradle bin
%~> env | grep PATH
PATH=/usr/local/bin:../.toolbox/bin:/opt/gradle/gradle-8.0.2/bin
```

**Validate Installation**:
```
~> gradle -v

------------------------------------------------------------
Gradle 8.0.2
------------------------------------------------------------

Build time:   2023-03-03 16:41:37 UTC
Revision:     7d6581558e226a580d91d399f7dfb9e3095c2b1d

Kotlin:       1.8.10
Groovy:       3.0.13
Ant:          Apache Ant(TM) version 1.10.11 compiled on July 10 2021
JVM:          17.0.6 (Amazon.com Inc. 17.0.6+10-LTS)
OS:           Mac OS X 12.6.3 x86_64

√[bdastur] javasamples/demo %~> 

```

## Gradle Appln/project setup.
Setting up a simple gradle app.

```
√[bdastur] notes/java %~> mkdir simpleApp
√[bdastur] notes/java %~> cd simpleApp 
√[bdastur] java/simpleApp %~> gradle init
Starting a Gradle Daemon (subsequent builds will be faster)

Select type of project to generate:
  1: basic
  2: application
  3: library
  4: Gradle plugin
Enter selection (default: basic) [1..4] 2

Select implementation language:
  1: C++
  2: Groovy
  3: Java
  4: Kotlin
  5: Scala
  6: Swift
Enter selection (default: Java) [1..6] 3

Split functionality across multiple subprojects?:
  1: no - only one application project
  2: yes - application and library projects
Enter selection (default: no - only one application project) [1..2] 1

Select build script DSL:
  1: Groovy
  2: Kotlin
Enter selection (default: Groovy) [1..2] 1

Generate build using new APIs and behavior (some features may change in the next minor release)? (default: no) [yes, 

Select test framework:
  1: JUnit 4
  2: TestNG
  3: Spock
  4: JUnit Jupiter
Enter selection (default: JUnit Jupiter) [1..4] 1

Project name (default: simpleApp): firstAWSApp
Source package (default: firstawsapp): 

> Task :init
Get more help with your project: https://docs.gradle.org/8.0.2/samples/sample_building_java_applications.html

BUILD SUCCESSFUL in 3m 25s
2 actionable tasks: 2 executed

```

### Running the Gradle app.

```
./gradlew run

```











