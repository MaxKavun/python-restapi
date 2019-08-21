FROM cruelgangsta/jenkins-slave-python
COPY app.py /root/
RUN ["python3","/root/app.py"]
