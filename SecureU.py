# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17Moiv63rH38ZSklniQvU1bbycDeswrrX
"""

# !pip install tldextract

# !pip install dnspython

# !sudo apt-get install nmap

# !pip install python-nmap

import nmap

import tldextract

import dns.resolver

from urllib import request

import ssl
import socket

import requests


def subdomainEnum_httpResponse(url):
    print("-----------------------------------------------------")

    # Returns a dictonary with the URL parts (i.e. domain, subdomain, suffix)
    url_parts = tldextract.extract(url)

    # wordlist.txt contains a list of all the popular subdomain strings
    file = open('wordlist.txt', 'r')
    content = file.read()

    dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
    # Using Google's Public DNS IP
    dns.resolver.default_resolver.nameservers = ['8.8.8.8']

    # setting timeout and lifetime to improve runtime by skipping unreachable urls
    dns.resolver.Resolver().timeout = 1
    dns.resolver.Resolver().lifetime = 1

    print("[+] Subdomains : ")
    count = 0

    subdomains = content.splitlines()

    for subdomain_loop in subdomains:

        try:

            # Trying to connect to the generated subdomain
            ip_value = dns.resolver.resolve(
                f'{subdomain_loop}.{url_parts.domain}.{url_parts.suffix}', 'A')
            if ip_value:

                # if subdomain exists, an HTTP request is made and its reponse code and status is returned
                # NOTE that an HTTP request is made instead of HTTPS.
                # This is done because site with HTTPS protocol will automatically redirect an HTTP request to an HTTPS request.
                # Hence, we do not have to explicitly check for HTTP and HTTPS while also including site with only HTTP.

                connection = request.urlopen(
                    f"http://{subdomain_loop}.{url_parts.domain}.{url_parts.suffix}", timeout=1)

                # - [code message] subdomain.domain.suffix
                print(
                    f'- [{connection.code} {connection.msg}] {subdomain_loop}.{url_parts.domain}.{url_parts.suffix}')
                count += 1

            else:
                pass
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.NoAnswer:
            pass
        except KeyboardInterrupt:
            quit()
        except Exception as e:
            pass
    print(f"\n[+] Total Subdomains Found : {count}")


def sslCheck(url):
    hostname = url
    ctx = ssl.create_default_context()

    print("-----------------------------------------------------")
    print("[+] SSL Details : ")

    # Creating a socket
    with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
        try:

            # Attempting to make a HTTPS(port number: 443) connection as only HTTPS sites contain and SSL certificate. URLs without and Secure Socket Layer will result in a TimeoutErron
            s.connect((hostname, 443))

            # retu
            cert = s.getpeercert()
            subject = dict(x[0] for x in cert['subject'])
            issued_to = subject['commonName']
            print("- SSL : Enabled")
            print(f"- issued_to : {issued_to}")
        except TimeoutError:
            print("- SSL : Disabled")


def portScanner(url):
    # This function returns the IPv4 address of the given URL.
    ip = socket.gethostbyname(url)

    print("-----------------------------------------------------")
    print("[+] Ports")

    # instantiate a PortScanner object
    nm = nmap.PortScanner()

    for port in range(1, 251):
        try:

            # the result is a dictionary containing
            # several information we only need to
            # check if the port is opened or closed
            # so we will access only that information
            # in the dictionary
            result = nm.scan(ip, str(port))

            port_status = (result['scan'][ip]['tcp'][port]['state'])

            print(f"Port {port}   : {port_status}")
        except:
            print(f"Cannot scan port {port}.")


def isXSSHeader(url):
    print("-----------------------------------------------------")
    print("[+] Header : ")

    try:
        # makes a GET request
        req = requests.get(f"http://{url}")
        # extracting 'X-XSS-Protection' from the headers dict from GET
        xssprotect = req.headers['X-XSS-Protection']
        if (xssprotect != "0"):
            print('X-XSS-Protection : Enabled')
        else:
            print('X-XSS-Protection : Disabled')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    a = input("[+] URL : ")
    subdomainEnum_httpResponse(a)
    sslCheck(a)
    portScanner(a)
    isXSSHeader(a)

isXSSHeader(a)
