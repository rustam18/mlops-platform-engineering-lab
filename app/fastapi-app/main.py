from fastapi import FastAPI
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
import time, os

app = FastAPI()

REQUEST_COUNT = Counter(
    'fastapi_requests_total',
    'Total inference requests',
    ['method', 'endpoint']
)

REQUEST_LATENCY = Histogram(
    'fastapi_request_latency_seconds',
    'Request latency in seconds',
    ['endpoint']
)

@app.get("/")
def root():
    start = time.time()
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    REQUEST_LATENCY.labels(endpoint='/').observe(time.time() - start)
    return {"model": os.getenv("MODEL_NAME", "default"), "status": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
