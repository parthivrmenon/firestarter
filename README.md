# firestarter
A POC for exploring doing blackbox synthetics with Target observability stack [Prometheus + Grafana]

## Getting started
```bash
# clean up existing minikube containers
minikube delete

# start a new minikube cluster
minikube start 

# install prometheus + grafana using helm (kube-prometheus-stack)
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack


# installl prometheus blackbox exporter
helm install prometheus-blackbox-exporter prometheus-community/prometheus-blackbox-exporter

# Accessing BlackBox Exporter endpoint @ http://127.0.0.1:8080
$POD_NAME = (kubectl get pods --namespace default -l "app.kubernetes.io/name=prometheus-blackbox-exporter,app.kubernetes.io/instance=prometheus-blackbox-exporter" -o jsonpath="{.items[0].metadata.name}") -replace '\r?\n',''
$CONTAINER_PORT = (kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}") -replace '\r?\n',''
kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT


export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=prometheus-blackbox-exporter,app.kubernetes.io/instance=prometheus-blackbox-exporter" -o jsonpath="{.items[0].metadata.name}")
export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
echo "Visit http://127.0.0.1:8080 to use your application"
kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT


# Example probe 
http://127.0.0.1:8080/probe?target=google.com&module=http_2xx





kubectl port-forward service/prometheus-grafana 80:80

# Exposing the Grafana UI
kubectl port-forward service/prometheus-grafana 80:80

# curl -u admin:prom-operator http://127.0.0.1/api/datasources









```
