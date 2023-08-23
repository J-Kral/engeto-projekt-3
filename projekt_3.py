import sys
import csv
from bs4 import BeautifulSoup
import requests

 
def check_arguments():
    if sys.argv[1].startswith("https://volby.cz/pls/ps2017nss/") == False:
        print("URL SHOULD START WITH https://volby.cz/pls/ps2017nss/")
        quit()
    elif len(sys.argv) != 3:
        print("MUST BY 2 ARGUMENTS: URL FILENAME")
        quit()
   

def stahuj_data():
    stranka = requests.get(sys.argv[1])
    return BeautifulSoup(stranka.text, "html.parser")    
    

def ziskat_obec(stranka):
    kod_obec = []
    link_obec = []
    href_all = stranka.find_all("a")
    for href_ in href_all:
        if href_.text.isnumeric() and len(href_.text) == 6:
            kod_obec.append(href_.text)
            link_obec.append("https://volby.cz/pls/ps2017nss/" + href_["href"])  #.encode('utf-8'))
    return kod_obec, link_obec


def ziskat_contents(previev_href):
    contents = ["code", "location", "registered", "envelopes", "valid"]
    previev_stranka = requests.get(previev_href)
    parsing_stranka = BeautifulSoup(previev_stranka.text, "html.parser")
    for subjekt in parsing_stranka.find_all("td")[10::5]:
        if subjekt.text != "-":
            contents.append(subjekt.text)
    return contents  

    
def add_obec_info(link_obec,code):        
    obec_x = [code]
    href_req = requests.get(link_obec)
    href_data = BeautifulSoup(href_req.text, "html.parser")
    obec_x.append(str(href_data.find_all("h3")[2].text).split(":")[1].strip()) # location 
    obec_x.append("".join(str(href_data.find_all("td")[3].text).split()))  # registered
    obec_x.append("".join(str(href_data.find_all("td")[4].text).split()))  # envelopes
    obec_x.append("".join(str(href_data.find_all("td")[7].text).split()))  # valid
    for party in href_data.find_all("td")[11::5]:
        if party.text != "-":
            obec_x.append(party.text)  # subjekt        
    return obec_x


def main():
    check_arguments()
    print("STAHUJI DATA Z VYBRANEHO URL:", sys.argv[1])
    stranka = stahuj_data()    
    kod_obec, link_obec = ziskat_obec(stranka)
    contents = ziskat_contents(link_obec[0])
    with open(sys.argv[2] + ".csv", "w", encoding='utf-8', newline="") as file:
        print("UKLADAM DO SOUBORU ",sys.argv[2],".csv\nZPRACOVANO %:", sep = '')
        file_csv = csv.writer(file, delimiter=";")
        file_csv.writerow(contents)
        numObec = len(kod_obec)
        step_msg = 0
        coefficient = 100 / numObec
        for i in range(len(kod_obec)):
            step_msg += 1
            if step_msg == 5:
                print(' ',int(i * coefficient),end="\r")
                step_msg = 0            
            file_csv.writerow(add_obec_info(link_obec[i],kod_obec[i]))            
        print(" 100  \nEND")

main()