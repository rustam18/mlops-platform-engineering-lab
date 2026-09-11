# K1 — Core Kubernetes Objects

**Context.** Needed a working ML inference service on Kubernetes to build
every later module (autoscaling, storage, RBAC) against — not a toy
example, something with real Deployment/Service/Config lifecycle.

**Challenge.** Coming from a telecom OSS/BSS and NFV/SDN background, the
mental model that needed rebuilding wasn't containers or orchestration —
it was Kubernetes' reconciliation loop and how Service-to-Pod routing
resolves purely through label selectors, not fixed addresses.

**Approach.** Deployed `fastapi-inference` (2 replicas, 512Mi limit),
exposed it via a ClusterIP `fastapi-svc`, externalized config through a
ConfigMap and Secret. Practiced deliberately breaking routing by editing
Pod labels, watching the Service silently stop selecting a Pod, and
diagnosing OOMKilled vs Pending failures by cause instead of guessing.

**Outcome.** Working baseline service other modules build on, plus a
concrete mental model: Deployment → ReplicaSet → Pod hierarchy, pod
template changes vs replica count changes, and why ConfigMap/Secret
separation isn't itself a security boundary — RBAC and vaults are.

## Files
- `fastapi-deployment.yaml`
- `fastapi-service.yaml`
- `fastapi-configmap.yaml`
- `fastapi-secret.example.yaml` — sanitized template; real value never committed
