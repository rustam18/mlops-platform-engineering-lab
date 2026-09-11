# MLOps Platform Engineering Lab

Hands-on lab documenting my transition from Senior DevOps / Integration Engineer
(12 years, telecom infrastructure — Jio, Globe, Etisalat, Batelco, Telenor, Ericsson)
to AI Platform / MLOps Engineering. Every manifest here was built and validated on
a local cluster, not copied from a tutorial.

## Structure

- `k1-core-objects/` — Kubernetes core objects: Deployment, Service, ConfigMap,
  label selector mechanics, reconciliation model
- `k2-hpa-custom-metrics/` — Custom metrics autoscaling pipeline for an ML
  inference workload (Prometheus + Prometheus Adapter + HPA)
- `k3-storage-rbac-networking/` — Persistent storage, RBAC, NetworkPolicy
  isolation (in progress)
- `app/fastapi-app/` — FastAPI inference service instrumented with
  `prometheus-client`

## Why this exists

Targeting AI Platform Engineer / MLOps Engineer roles (IC track) at GCCs in
Delhi NCR. This repo is the proof-of-work layer behind that transition —
12 years of telecom-scale infrastructure experience applied to AI infra.

## Environment

Windows + WSL2, Rancher Desktop (k3s), containerd runtime.
