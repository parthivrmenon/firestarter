# Prometheus + Grafana monitoring for MongoDB
## Getting started
- [Minikube](#minikube)
- [Installing prometheus via Helm](#installing-prometheus-via-helm)
- []


### Minikube
```bash
# Start a minikube cluster
minikube start --cpus 4 --memory 8192
```

### Installing Prometheus via Helm
```bash

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack


```

### Expose prometheus and grafana UIs
```bash
# to access prometheus UI at http://localhost:9090
kubectl port-forward service/prometheus-kube-prometheus-prometheus 9090
kubectl port-forward deployment/prometheus-grafana 3000


```
### Deploying mongodb application for testing
```bash
kubectl apply -f mongodb.yaml

```
### Deploying Mongodb exporter via Helm
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install mongodb-exporter prometheus-community/prometheus-mongodb-exporter -f values.yaml

#kubectl port-forward service/mongodb-exporter-prometheus-mongodb-exporter 9216

```


### Adding a ServiceMonitor
```bash
release: prometheus
```