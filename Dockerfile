FROM alpine:3.12.3
COPY app.py /root/
ENTRYPOINT ["python3","/root/app.py"]
