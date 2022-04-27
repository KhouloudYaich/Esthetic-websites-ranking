from urllib.parse import urlparse

#Get domain name (example.com) ( exp : abdominoplastie-tunisie.fr )
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

#Get the name of the project (exp : 'abdominoplastie-tunisie' )
def get_project_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2]
    except:
        return ''


#Get sub domain name (name.example.com) ( exp : 'www.abdominoplastie-tunisie.fr')
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
