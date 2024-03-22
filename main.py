import requests
from helpers import get_token
###Changes every 5 minutes
headers = {
    "Authorization" : get_token()
}

getStudentResponse = requests.get('https://micaapi.msuiit.edu.ph/api/info/v2/student/get_info?studid=2019-8904', headers=headers)
getProspectusResponse = requests.get('https://micaapi.msuiit.edu.ph/api/info/v1/student/view/prospectus?studid=2019-8904', headers=headers)

print(getStudentResponse.text)
print(getProspectusResponse.text)


