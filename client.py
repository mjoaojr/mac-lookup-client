import requests

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

m = ler_csv()
print(m)