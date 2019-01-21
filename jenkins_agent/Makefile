build: Dockerfile
	docker build --tag brdagent:0.1 .
run: build
	docker rm -f build_agent
	docker run -it --name build_agent \
		--network host \
		--env "EXTRA_PARAMS=-executors 3 -master http://localhost:8085/jenkins-scy/ -username admin -password password -labels  build_agent -name build_agent" \
        -v /var/run/docker.sock:/var/run/docker.sock \
		-v /Users/behzad.dastur/code/KATAS/jenkins_agent:/root \
		-v /tmp/jenkins-data:/var/jenkins_home \
		brdagent:0.1
