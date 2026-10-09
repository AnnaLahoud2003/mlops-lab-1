FROM python:3.11-slim

# Pin the same mlflow version as the client in uv.lock (3.16.1)
RUN pip install --no-cache-dir mlflow==3.16.1

EXPOSE 5000

# --artifacts-destination: mlflow stores artifacts there AND serves them over HTTP,
#   so other containers download the model through http://mlflow:5000
#   instead of a file path that only exists inside this container.
# --allowed-hosts: mlflow 3.x rejects unknown Host headers; "mlflow" is the
#   Compose service name the inference container will use.
CMD ["mlflow", "server", \
     "--host", "0.0.0.0", "--port", "5000", \
     "--backend-store-uri", "sqlite:////mlflow-data/mlflow.db", \
     "--artifacts-destination", "/mlflow-data/mlartifacts", \
     "--allowed-hosts", "mlflow,mlflow:*,localhost,localhost:*,127.0.0.1,127.0.0.1:*"]