from tld import get_tld

def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name


# print(get_domain_name('https://thenewboston.com/'))
#print(get_domain_name('http://www.meetup.com/'))