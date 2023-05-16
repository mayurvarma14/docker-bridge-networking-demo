FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY service3.py .

CMD ["python","-u", "service3.py"]
