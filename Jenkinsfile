pipeline {
	agent { label 'py-app' } 
	stages {
		stage('Docker build') {
			steps {
				sh "docker build -t cruelgangsta/python-restapi-flask:$BUILD_NUMBER ."
			}
		}

		stage('Push to the docker hub') {
			steps {
				sh "docker push cruelgangsta/python-restapi-flask:$BUILD_NUMBER"
			}
		}

		stage('Deploy to staging') {
			steps {
				sh "docker run -d --rm -p 8765:5000 --name flask-app cruelgangsta/python-restapi-flask:$BUILD_NUMBER"
				sleep 60
			}
		}
	}

	post {
		always {
			sh "docker stop flask-app"
		}
	}
}
