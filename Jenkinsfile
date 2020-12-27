pipeline {
	agent any 
	stages {
		stage('Docker build') {
			steps {
				sh "docker build -t wsgi-implementation:$BUILD_NUMBER ."
			}
		}

		stage('Push to the docker hub') {
			steps {
				echo 'sh "docker push cruelgangsta/python-restapi-flask:$BUILD_NUMBER"'
			}
		}

		stage('Deploy to staging') {
			steps {
				//sh "docker run -d --rm -p 8765:5000 --name flask-app cruelgangsta/python-restapi-flask:$BUILD_NUMBER"
				sleep 20
			}
		}
	}
}
