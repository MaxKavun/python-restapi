pipeline {
	agent { label 'py-app' } 
	stages {
		stage('Package') {
			steps {
				sh "python3 app.py"
				sleep 10
				sh "killall python3 app.py"
			}
		}

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
