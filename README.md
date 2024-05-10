# firestarter
This project contains all the scripts and test environments to migrate TM observability assets onto 1SP.


## Audit
```bash

export GRAFANA_URL="https://grafana.example.com"
export GRAFANA_USER="changeme"
export GRAFANA_PASS="changeme"

source venv/bin/activate
python audit/main.py

```

## Getting started
```bash
# clean up existing minikube containers
minikube delete

# start a new minikube cluster
minikube start 


# install and configure prometheus-operator
kubectl apply -f prometheus-operator/namespace.yaml 
kubectl apply --server-side -f prometheus-operator/crd/
kubectl apply -f prometheus-operator/rbac/
kubectl apply -f prometheus-operator/deployment/

# install and configure prometheus
kubectl apply -f prometheus/

# ensure pods & services are running
kubectl get pods -n monitoring
NAME                                   READY   STATUS    RESTARTS   AGE
prometheus-main-0                      2/2     Running   0          3m55s
prometheus-operator-5895f6fbd8-2zqkw   1/1     Running   0          9m25s

kubectl get services -n monitoring
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
prometheus-operated   ClusterIP   None         <none>        9090/TCP   3m28s

# expose prometheus UI at http://localhost:9090
kubectl port-forward svc/prometheus-operated 9090 -n monitoring

# install grafana via helm
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm install grafana grafana/grafana


# install prometheus + grafana using helm (kube-prometheus-stack)
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack

# get your grafana 'admin' password
kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

# expose Grafana UI
export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=grafana" -o jsonpath="{.items[0].metadata.name}")
kubectl --namespace default port-forward $POD_NAME 3000
```











# Additional
```bash
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
