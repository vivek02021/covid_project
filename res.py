import requests
import json
import matplotlib.pyplot as plt
import pickle

def refresh_data():

    state_url = "https://api.covid19india.org/state_district_wise.json"

    state_response = requests.get(state_url)
    state_data = json.loads(state_response.text)


    for state in state_data:
        for district in state_data[state]['districtData']:
            
            dist = state_data[state]['districtData'][district]
            
            labels = []
            sizes = []


            if dist["active"] != 0:
                labels.append("active")
                sizes.append(dist["active"])



            if dist["deceased"] != 0:
                labels.append("deceased")
                sizes.append(dist["deceased"])


            if dist["recovered"] != 0:
                labels.append("recovered")
                sizes.append(dist["recovered"])
            
                    
            plt.figure(figsize=(8,8))
            plt.pie(sizes, labels=labels, autopct="%1.1f%%")
            plt.savefig("static/images/{}/{}.png".format(state,district))
            plt.close()
        
                
        
    file = open("state_data.ser","wb")
    pickle.dump(state_data,file)
    file.close() 