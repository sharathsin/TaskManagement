from django.http import HttpResponse
from prometheus_client import generate_latest
from prometheus_client import Counter, Histogram, start_http_server

REQUEST_COUNT = Counter('user_service_requests_total', 'Total number of requests to the user service', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('user_service_request_latency_seconds', 'Latency of requests to the user service')
def metrics_view(request):
    metrics_page = generate_latest()
    return HttpResponse(metrics_page, content_type="text/plain")
def track_request(method, endpoint):
    REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()

def track_latency(duration):
    REQUEST_LATENCY.observe(duration)