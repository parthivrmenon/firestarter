import requests
import json


USER="alerts"
PASS="63gab4qLWUjgt"

GRAFANA_HOST = "https://grafana.telemessage.com"
DATASOURCE_ID = "2"


# Get prometheus jobs from targets
url = f'{GRAFANA_HOST}/api/datasources/proxy/{DATASOURCE_ID}/api/v1/query'
params = {"query": "up"}
#params = {"query" : "{job='prometheus/keeper-podmonitor'}"}
# params = {"query" : "count({job="prometheus/keeper-podmonitor"})" }


response = requests.get(url, params=params, auth=(USER,PASS))
targets = response.json()["data"]["result"]

job_list = []
for target in targets:
    j = target["metric"]["job"]
    if j not in job_list:
        job_list.append(j)




for j in job_list:
    #param_string_reference = "query={job='prometheus/haraka-monitor'}"
    #j = 'prometheus/haraka-monitor'
    param_string = f"query={{job='{j}'}}"

    #print(param_string, param_string_reference)

    try:
        response = requests.get(url, params=param_string, auth=(USER,PASS))
        print(j,len(response.json()["data"]["result"]), sep=",")
    except Exception as err:
        print(j,"-1",sep=",")


# for target in data["data"]["result"]:
#     print(target["metric"]["instance"], target["metric"]["job"])



