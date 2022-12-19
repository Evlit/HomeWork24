FROM python:3.10
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# COPY utils.py .
COPY data/apache_logs.txt data/apache_logs.txt
# COPY docker_config.py default_config.py
#CMD flask run -h 0.0.0.0 -p 80
CMD ["sh","entrypoint.sh"]