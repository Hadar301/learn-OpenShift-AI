FROM registry.access.redhat.com/ubi9/python-311

WORKDIR /app
COPY app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

USER 1001

CMD ["streamlit", "run", "app/app.py", "--server.port=8501"]
