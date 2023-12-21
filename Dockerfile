FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "./your-daemon-or-script.py"]
#FROM nginx
#Copy *.html /usr/share/nginx/html
