from prometheus_client import Counter, Histogram, start_http_server
import time

# Define metrics


def start_metrics_server():
    start_http_server(8005)  # Expose metrics on port 8005
    print("Prometheus metrics server started on port 8005")


