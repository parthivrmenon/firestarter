# Prometheus
# PromQL to scrape all targets, jobs : 
#  https://grafana.telemessage.com/api/datasources/proxy/2/api/v1/query?query={job='prometheus/haraka-monitor'}




import csv
import requests


def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)


# Configuration
GRAFANA_USER = "alerts"
GRAFANA_PASS = "63gab4qLWUjgt"
GRAFANA_QUERY_URL = "https://grafana.telemessage.com/api/datasources/proxy/2/api/v1/query?query="
GRAFANA_SEARCH_API = " https://grafana.telemessage.com/api/search?query="



# targets.csv
# Instance, Job
QUERY_UP = "up"
URL = f"{GRAFANA_QUERY_URL}{QUERY_UP}"


r = requests.get(URL,auth=(GRAFANA_USER, GRAFANA_PASS)).json()

jobs = []

targets_data = [
    ['Instance','Job']
]

print("Collecting prometheus targets...")
for d in r["data"]["result"]:
    i = d['metric']['instance']
    j = d['metric']['job']
    if j not in jobs:
        jobs.append(j)
    
    row = [i,j]
    targets_data.append(row)
    # print(i,j,sep=",")

print("Writing to targers.csv ...")
write_to_csv('targets.csv', targets_data)
    
    # title = d['title']
    # try:
    #     folder = d['folderTitle']
    # except Exception as e:
    #     folder= 'ERR'
    # print(title, folder, sep=',')

metric_data = [
    ['Job', 'Metrics']
]

print("Collecting prometheus metrics counts...")
for JOB in jobs:
    #JOB = 'prometheus/haraka-monitor'
    JOB_METRIC_COUNT = f"count({{job='{JOB}'}})"
    URL = f"{GRAFANA_QUERY_URL}{JOB_METRIC_COUNT}"
    r = requests.get(URL,auth=(GRAFANA_USER, GRAFANA_PASS)).json()
    c = r['data']['result'][0]['value'][1]
    row = [JOB, c]
    metric_data.append(row)
    #print(JOB,c, sep=",")

print("Writing to metrics.csv ...")
write_to_csv('metrics.csv', metric_data)



print("Collecting Grafana dashboards...")
GRAFANA_QUERY_ALL_DASHBOARDS = "&type=dash-db"
URL = f"{GRAFANA_SEARCH_API}{GRAFANA_QUERY_ALL_DASHBOARDS}"
grafana_dashboard_data = [
    ['Dashboard','Folder']
]
r = requests.get(URL,auth=(GRAFANA_USER, GRAFANA_PASS)).json()
for d in r:
    row = [d["title"],d["folderTitle"]]
    grafana_dashboard_data.append(row)

print("Writing to dashboards.csv ...")
write_to_csv('dashboards.csv', grafana_dashboard_data)



