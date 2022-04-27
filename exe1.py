from main import Main
def file_to_set(file_name):
    results = []
    with open(file_name, 'rt') as f:
        for line in f:
            results.append(line.replace('\n', ''))
    return results

path='webCrawler/Site_esthétique.txt'

urlSet=file_to_set(path)


for url in urlSet:
    main=Main(url)
    main.create_workers()
    main.crawl()
   
    LIST=['https://www.carthagomed.com',
      'https://www.chirurgiepro.net',
      'https://www.centremahassen.com/',
      
        'https://www.dr-samia-aoun.com/',
      'https://cliniquelesoliviers.net/',
      'https://www.drbalti.com/',
      'https://www.clinique-esthetique-carthagene.com/',
      'http://www.amirchaibi.com/',
      'http://www.dr-houda-kebaili.com/',
      'https://www.docteur-sami-mezhoud.com/',
      'https://www.docteur-hichem-mahmoud.com/',
      'https://www.dr-mourad-zinelabidine.com/',
      'https://www.clinique-elyosr.com/',
      'https://www.dr-chiraz-bouzguenda.fr/',
      'https://www.drgharbinedra.com/',
      'https://www.dr-benamara-imene.com/  ',
      'https://medical-travel.fr/tarifs/ ',
      'https://venus-estetika.com/ ',
      'https://clinique-saint-augustin.com/ ',
      'https://chirurgieentunisie.com/ ',
      'https://www.tunisieesthetique.fr/clinique/',
      'https://idealmed-tunisie.com/',
      'https://www.chirurgieesthetiquetunisie.fr/',
      'https://medicalys-tunisie.com/',
      'https://www.dr-benjemaa.com/',
      'https://www.medespoir.fr/medecine-esthetique-tunisie/',
      'https://www.cosmetic-tour.com/clinique-les-jasmins-tunisie/',
      'https://www.aviscliniques.com/clinique/centre-international-carthage-medical/',
      'https://www.chirurgie-esthetique-entunisie.com/',
      'https://medica-travel.com/',
      'https://www.esthetic-planet.com/chirurgie-esthetique-tunisie.html',
      'https://tunisie-beauty-center.com/',
      'https://www.cosmeticatravel.com/cliniques-esthetiques-tunisie.php',
      'https://www.dr-alyagargouri.com/',
      'https://medcare-vacances.ca/',
      'https://www.chirurgie-esthetique-tunis.com/',
      'https://www.univers-med.com/',
      'https://lerdvmedical.tn/index.php/archives/doctors/dr-yosra-labidi-mnif',
      'https://twintravelmedical.com/',
      'https://www.journeycaremedical.com/fr/',
      'https://www.labelesthetique.com/label-esthetique/cliniques/',
      'https://doctour.com.tn/chirurgie-bariatrique-tunisie/',
      'https://medecine-esthetique-paris.net/clinique-esthetique-tunisie/',
      'https://anismrabet.com/a-propos/',
      'https://www.axessmedical.com/lagence/cliniques/',
      'https://www.medica-tour.fr/docteur-hichem-mahmoud/',
      'http://dermatologie-esthetique-tunisie.com/',
      'https://docteur-benromdhane.com/',
      'http://www.chedlybouzouaya.com/',
      'https://www.taoufikhospitalsgroup.com/nos-cliniques/hannibal-clinique/',
      'https://www.sejour-medical.fr/',
      'https://www.e2a-international.com/tarifs-chirurgie-esthetique-bariatrique-tunisie#content',
      'https://www.aram-esthetique.com/',
      'http://www.theesthetique.com/',
      'https://www.clinique-hannibal-tunisie.fr/',
      'http://www.clinica-chirurgie-esthetique.com/',
      'https://www.esthetique-tunisie.fr/',
      'https://medical-travel.fr/tarifs/' ,
      'https://chirurgieentunisie.com/ ',
      'https://www.chirurgieesthetiquetunisie.fr/',
      'https://medicalys-tunisie.com/',
      'https://www.medespoir.fr/medecine-esthetique-tunisie/',
      'https://www.dr-djemal.com/',
      'https://www.clinique-espoir-tunisie.com/',
      'https://www.chirurgien-esthetique-tunisie.fr/clinique-la-soukra-tunisie',
      'http://www.clinique-internationale-esthetique-tunis.com/',
      'https://www.centre-international-carthage-medical.com/',
      'https://www.clinique-hannibal.com/chirurgie-esthetique-tunisie/',
      'https://www.ramcomedical.com/',
      'http://centre-aesthetica.com/']


abdominoplastie-tunisie,https://www.abdominoplastie-tunisie.fr,2,2850,0
carthagomed,https://www.carthagomed.com,37,2064,0
chirurgiepro,https://www.chirurgiepro.net,47,1820,1

https://cliniquelesoliviers.net/