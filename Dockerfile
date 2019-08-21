FROM cruelgangsta/jenkins-slave-python
COPY app.py /root/
ENTRYPOINT ["python3","/root/app.py"]
