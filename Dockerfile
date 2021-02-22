FROM python:3.7-slim-stretch
RUN apt-get update
RUN apt-get install -y --no-install-recommends git
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD streamlit run main.py