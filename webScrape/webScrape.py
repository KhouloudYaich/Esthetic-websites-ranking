from bs4 import BeautifulSoup
import pandas as pd
import requests
import os

### Read a file and convert each line to list items ###
def file_to_list(file_name):
    results = []
    with open(file_name, 'rt') as f:
        for line in f:
            results.append(line.replace('\n', ''))
    return results

### collecter les noms des fichers qui contiennet dans un directory ###
def folder_name(directory):
    filenames = os.listdir(directory)  # get all files' and folders' names in this directory
    siteCrawled = []
    for filename in filenames:  # loop through all the files and folders
        filePath = os.path.join(os.path.abspath(directory), filename)
        if os.path.isdir(filePath):  # check whether the current object is a folder or not
            siteCrawled.append(filePath)
    return siteCrawled

### chercher les mots docteur , doctor , .. dans les balizes html definis dans une liste listBalize ###
def citationMedecin(listBalize, url):
    dict = {"doctor": 0}
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    for balize in listBalize:
        imgs = soup.findAll(balize)
        for i in imgs:
            if (('docteur' in i.text.lower()) or ('dr' in i.text.lower()) or ('doctor' in i.text.lower()) or (
                    'chirurgiens' in i.text.lower()) or ('chirurgienne' in i.text.lower())):
                dict["doctor"] = 1
            break
    print("citationMedecin ok")
    return dict
    
### calculer le nombre d'interventions ###
def Nbre_Iinterventions(BaseUrl):
    response = requests.get(BaseUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.select("nav li a")
    ListIntervention = []
    data
    for i in data:
        if ("href" in str(i)):
            ListIntervention.append(i)
    NbreIntervention = len(ListIntervention) - 5
    if (NbreIntervention == -5):
        NbreIntervention= None
    print("nbre interventions ok")
    return NbreIntervention

### calculer le nombre d'images ###
def Nom_Agence(base_url):
    i = base_url.find('.') + 1
    j = base_url[i:].find('.')
    nomAgence = base_url[i:i + j]
    print("nom agence ok")
    return nomAgence

### calculer la moyenne des prix ###
def Calcul(nbInterventions, tarifUrl):

        prix = 0
        marge = 1
        try:
            read_table = pd.read_html(tarifUrl)

            for table in read_table:
                colonnePrix = list(table.iloc[:, 1].values)
                for ch in colonnePrix:
                    ch = str(ch)
                    fin = 0
                    if ch.find("$") != -1:
                        fin = ch.index("$")
                        marge = 3
                    elif ch.find("€") != -1:
                        fin = ch.index("€")
                        marge = 3.25
                    elif (ch.find("DT") != -1):
                        fin = ch.index("DT")
                        marge = 1
                    debut = fin
                    while (not (ch[debut - 1].isalpha()) and debut != 0):
                        debut -= 1
                    if (debut != fin):
                        chainePrix = ch[debut:fin].replace(" ", "")
                        prix += int(chainePrix)
            prix = prix*marge
            Price_Average = prix // nbInterventions
        except:
            Price_Average = None
        print("price average ok")
        return Price_Average

########## start web Scrape ##########
siteCrawled = folder_name("..\webCrawler\siteCrawled")
rows = []

for folder in siteCrawled:
    allUrls = file_to_list(folder + "\crawled.txt")
    base_url = allUrls[0]

    nomAgence = Nom_Agence(base_url)
    nbInterventions = Nbre_Iinterventions(base_url)
    print("crawling ok")

#######################################
    Reviews = 0
    Before_After_Images = 0
    tarifUrl = ''
    for url in allUrls:
        if ((url.find("tarif") != -1) or (url.find("prix") != -1)):
            tarifUrl = url
        if ((url.find("temoignages") != -1) or (url.find("avis") != -1)):
            Reviews = 1
        if (url.find("avant-apres") != -1) :
            Before_After_Images = 1
        if (tarifUrl != ''):
            break
    Price_Average = None
    if (tarifUrl != ''):
        Price_Average = Calcul(nbInterventions, tarifUrl)
#######################################

    MedecinUrl = ''
    existence_of_doctors = 0
    for url in allUrls:
        if ((url.find("chirurgien") != -1) or  (url.find("medecin") != -1) or (url.find("doctor") != -1)):
            existence_of_doctors = 1
        else:
            dict = citationMedecin(['h1', 'h2', 'h3', 'h4', 'p', 'strong', 'span', 'div'], url)
            existence_of_doctors = dict["doctor"]

    row = []
    row.append(nomAgence)
    row.append(base_url)
    row.append(existence_of_doctors)
    row.append(Reviews)
    row.append(nbInterventions)
    row.append(Price_Average)
    row.append(Before_After_Images)

    rows.append(row)

dataset = pd.DataFrame(rows, columns=["Agency_Name", "url", "existence_of_doctors", "Reviews", "Number_of_interventions", "Price_Average", "Before_After_Images"])
dataset.to_csv('realbase.csv', encoding='UTF-8', index=False)
print("it's ok")
