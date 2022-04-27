from main import Main

#Les 3 urls des sites qu'on va scrapper
def file_to_set(file_name):
    results = []
    with open(file_name, 'rt') as f:
        for line in f:
            line=line.replace("' ", '')
            results.append(line.replace('\n', ''))
    return results

path="rowData.txt"


URLs=file_to_set(path)



for url in URLs:
    main=Main(url) #instanciation de main qui va definir les attr suivant pour chaque home page (home_page ,project_name ,DOMAIN_NAME
    # ,queue_file ,crawled_file ,number_of_threads ,queue )
    main.create_workers()
    main.crawl()

   

