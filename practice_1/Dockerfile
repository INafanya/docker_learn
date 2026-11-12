FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./write_data.py /app
RUN pip install --no-cache-dir pymongo
CMD ["python", "./write_data.py"]