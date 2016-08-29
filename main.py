from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *
import os



ROOT_DIR = 'companies'
create_dir(ROOT_DIR)


def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(domain_name)
    nmap = get_nmap('-F', ip_address)
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, nmap, robots_txt, whois)
    print(domain_name)
    print(ip_address)
    print(nmap)
    print(whois)


def gather_info_Without_Robots(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(domain_name)
    nmap = get_nmap('-F', ip_address)
    whois = get_whois(domain_name)
    create_report_Without_Robots(name, url, domain_name, nmap, whois)
    print(domain_name)
    print(ip_address)
    print(nmap)
    print(whois)





def create_report(name, full_url, domain_name, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots.txt', robots_txt)
    write_file(project_dir + '/whois.txt', whois)

def create_report_Without_Robots(name, full_url, domain_name, nmap, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/whois.txt', whois)

#User Input
print('Enter a website name to scan:')
webName = input()

print('Enter the website\'s url:')
weburl = input()

gather_info(webName, weburl)


#gather_info(e1, e2)


#gather_info_Without_Robots('gpbuddy','http://www.gpbuddy.ie/')

#gather_info('Star Wars', 'http://www.starwars.com/')

#gather_info('Reddit', 'https://www.reddit.com')

#gather_info('Facebook', 'https://www.facebook.com/')

#gather_info_Without_Robots('Twitter', 'https://twitter.com/')

#gather_info('TheJournal', 'http://www.thejournal.ie/')

#gather_info_Without_Robots('meetup','http://www.meetup.com')

#gather_info('Pinterest','https://www.pinterest.com/')

#gather_info_Without_Robots('Cineworld','http://www.cineworld.ie/')

#gather_info('BBC','http://www.bbc.com/')

#gather_info_Without_Robots('BBC','http://www.bbc.com/')

#gather_info_Without_Robots('Least I Could Do','http://www.leasticoulddo.com/')


##gather_info(e1,e2)

