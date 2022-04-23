import requests
import json
result = requests.post("http://46.252.16.186:8469/api/v1/partners/check_mail",
                               json={
                                   "mail": "Ohne E-Mail - 2022-04-21T12:04:05"
                               }
                               ).json()
print(result)