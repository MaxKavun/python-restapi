pipeline {
	agent { label 'py-app' } 
	stages {
		stage('Docker build') {
			steps {
				sh "docker build -t cruelgangsta/python-restapi-flask ."
			}
		}

		stage('Deploy to staging') {
			steps {
				sh "docker run -d --rm -p 8765:8080 --name flask-app cruelgangsta/python-restapi-flask"
			}
		}
	}
}
