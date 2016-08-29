from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *
import os
from tkinter import *

ROOT_DIR = 'companies'
create_dir(ROOT_DIR)



############### GUI #########
def show_entry_fields():
   print("Website Name: %s\nURL: %s" % (WebsiteName.get(), URL_Name.get()))

master = Tk()
Label(master, text="Website Name").grid(row=0)
Label(master, text="URL").grid(row=1)

WebsiteName = Entry(master)
URL_Name = Entry(master)

WebsiteName.grid(row=0, column=1)
URL_Name.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Scan', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )

#############################################


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

