import requests
from get_token import get_token
import json
###Changes every 5 minutes


def write_file(filename, data):
    f = open(filename, 'w')
    f.write(data)
    f.close

def main():

    token = get_token()

    headers = {
        "Authorization" : token
    }

    for i in range(2019, 2020):
        for j in range(500, 520):
            idnum = f"{str(i).zfill(4)}-{str(j).zfill(4)}"

            getStudentResponse = requests.get(f'https://micaapi.msuiit.edu.ph/api/info/v2/student/get_info?studid={idnum}', headers=headers)
            getProspectusResponse = requests.get(f'https://micaapi.msuiit.edu.ph/api/info/v1/student/view/prospectus?studid={idnum}', headers=headers)


            write_file(f'prospectus/{idnum.split("-")[0]}/{idnum}.json', getProspectusResponse.text)
            write_file(f'student_info/{idnum.split("-")[0]}/{idnum}.json', getStudentResponse.text)

            student_info = json.loads(getStudentResponse.text)
            prospectus = json.loads(getProspectusResponse.text)

            try: 
                if(student_info['message'] == 'Token is invalid' or prospectus['message' == 'Token is invalid']):
                    headers = {
                        "Authorization": get_token()
                    }
            except:
                pass
    
if __name__ == "__main__":
    main()
