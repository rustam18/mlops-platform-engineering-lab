# K2 — HPA and Custom Metrics Scaling

**Context.** An ML inference workload needs to scale on actual demand,
not on a proxy metric that doesn't reflect load.

**Challenge.** Built and tested CPU-based HPA first (`hpa-fastapi-cpu.yaml`)
and confirmed it directly: CPU-bound autoscaling fails for inference
workloads, because request load and CPU usage don't move together for
this kind of service.

**Approach.** Instrumented the FastAPI app with `prometheus-client`,
wired a `ServiceMonitor` to scrape it, ran Prometheus Adapter to expose
`fastapi_requests` as a custom metric, and rebuilt the HPA
(`hpa-fastapi-custom.yaml`) against that instead of CPU. Debugged the
full chain when metrics silently didn't appear — traced it to the
Service object needing an explicit label (not just a selector) for
`ServiceMonitor` discovery, and the Service port needing a name for the
endpoint reference to resolve.

**Outcome.** Working 5-layer custom metrics pipeline (App → ServiceMonitor
→ Prometheus → Adapter → HPA), HPA scaling 2→6 replicas on real request
rate, 5-minute scale-down stabilization window understood and observed
in practice, not just read about.

## Files
- `hpa-fastapi-cpu.yaml` — the version that didn't work, kept intentionally
- `hpa-fastapi-custom.yaml` — the working version
- `servicemonitor-fastapi.yaml`
- `fastapi-with-metrics-config.yaml`
