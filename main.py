import requests


###Changes every 5 minutes
headers = {
    "Authorization" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Impvc2h1YWtlbmFuLmNpbmNoZXNAZy5tc3VpaXQuZWR1LnBoIiwiaWF0IjoxNzExMDk3OTI2LCJleHAiOjE3MTEwOTk3MjZ9.MhwP1YChu714PqneNNDeEbdg7s0R8gVh5ZWrOdOhYl0"
}

getStudentResponse = requests.get('https://micaapi.msuiit.edu.ph/api/info/v2/student/get_info?studid=2019-8904', headers=headers)
getProspectusResponse = requests.get('https://micaapi.msuiit.edu.ph/api/info/v1/student/view/prospectus?studid=2019-8904', headers=headers)

print(getStudentResponse.text)
print(getProspectusResponse.text)


