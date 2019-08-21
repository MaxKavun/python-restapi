FROM cruelgangsta/jenkins-slave-python
COPY app.py .
ENTRYPOINT ['python3','app.py']
