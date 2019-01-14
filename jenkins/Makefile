build: Dockerfile
	docker build --tag brdjenkins:0.1 .

test: build
	docker rm -f brdjenkins
	docker run -it --name brdjenkins \
		-p 8085:8080 \
		-v jenkins-data:/var/jenkins_home \
		-v /var/run/docker.sock:/var/rrun/docker.sock \
		-v /Users/behzad.dastur/code/KATAS/jenkins:/home \
		brdjenkins:0.1

