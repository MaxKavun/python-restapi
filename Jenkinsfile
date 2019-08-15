pipeline {
	agent { label 'py-app' } 
	stages {
		stage('Package') {
			steps {
				sh "python3 app.py"
			}
		}

		stage('Docker build') {
			steps {
				sh "docker build -t cruelgangsta/python-restapi-flask ."
			}
		}
	}
}