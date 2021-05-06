import requests
import json

def ler_csv():
    macs = {}
    with open('macs.csv', "r") as fp:
        lines = fp.readlines()
        #macs = [line.rstrip() for line in lines]
        # mesmo coisa
        if lines:
            for line in lines:
                line = line.rstrip()
                line_array = line.split(";")
                ip = line_array[0]
                mac = line_array[1]
                macs[ip] = mac

    return macs

def buscar_vendor(mac_address):
    url = "https://ckytpcuse7.execute-api.us-east-1.amazonaws.com/prod/api/v1"
    url = f"{url}/macs/{mac_address}"

    response = requests.get(url)
    if response.status_code==200:
        dic = json.loads(response.text)
        return dic
    else:
        print("Erro ao fazer request")
    

macs_dic = ler_csv()
macs=list(macs_dic.values())
mac_exemplo = macs[0]

dic = buscar_vendor(mac_exemplo)
fabricante = dic.get('vendor')

print(f"O fabricante do MAC: {mac_exemplo} é {fabricante}")