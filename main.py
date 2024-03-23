import requests
from get_token import get_token
import json
import threading
from datetime import datetime

def write_file(filename, data):
    f = open(filename, 'w')
    f.write(data)
    f.close

def main():

    token = get_token()

    headers = {
        "Authorization" : token
    }


    def fetch_data(idnum, TokenChecker):
        print(f"Fetching Student: {idnum}")
        getStudentResponse = requests.get(f'https://micaapi.msuiit.edu.ph/api/info/v2/student/get_info?studid={idnum}', headers=headers)
        getProspectusResponse = requests.get(f'https://micaapi.msuiit.edu.ph/api/info/v1/student/view/prospectus?studid={idnum}', headers=headers)


        write_file(f'prospectus/{idnum.split("-")[0]}/{idnum}.json', getProspectusResponse.text)
        write_file(f'student_info/{idnum.split("-")[0]}/{idnum}.json', getStudentResponse.text)
        
        TokenChecker.append({"responses" : [getStudentResponse, getProspectusResponse]})        
        return [getStudentResponse, getProspectusResponse]


    for i in range(2019, 2025):
        max_id = 10000
        num_threads = 50

        for j in range(0, max_id, num_threads):

            TokenChecker = []

            threads = []

            for k in range(num_threads):
                idnum = f"{str(i).zfill(4)}-{str(j + k).zfill(4)}"
                t = threading.Thread(target=fetch_data, args=(idnum, TokenChecker,))
                t.daemon = True
                threads.append(t)
            
            for k in range(num_threads):
                threads[k].start()

            for k in range(num_threads):
                threads[k].join()

            getStudentResponse, getProspectusResponse = TokenChecker[len(TokenChecker) - 1]['responses'] 

            student_info = json.loads(getStudentResponse.text)
            prospectus = json.loads(getProspectusResponse.text)

            try: 
                if(student_info['message'] == 'Token is invalid' or prospectus['message' == 'Token is invalid']):

                    print(f"Change Token at: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")

                    headers = {
                        "Authorization": get_token()
                    }

                    threads = []

                    for k in range(num_threads):
                        idnum = f"{str(i).zfill(4)}-{str(j + k).zfill(4)}"
                        t = threading.Thread(target=fetch_data, args=(idnum, TokenChecker,))
                        t.daemon = True
                        threads.append(t)
                    
                    for k in range(num_threads):
                        threads[k].start()

                    for k in range(num_threads):
                        threads[k].join()
            except:
                pass
    
    print("Fetching Done.")
                
    
if __name__ == "__main__":
    main()
