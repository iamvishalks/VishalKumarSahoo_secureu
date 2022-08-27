
# VishalKumarSahoo_secureu

This repository is a response to Secure U's Python Developer Assignment.





## Packages
In this section, we look at all the packages that were used in the Assignment.

import nmap

( !sudo apt-get install nmap )

( !pip install python-nmap )


import tldextract

( !pip install tldextract ) 

import dns.resolver

( !pip install dnspython )

from urllib import request

import ssl

import socket

import requests
## Packages
In this section, we look at all the packages that were used in the Assignment.

import nmap

( !sudo apt-get install nmap )

( !pip install python-nmap )


import tldextract

( !pip install tldextract ) 

import dns.resolver

( !pip install dnspython )

from urllib import request

import ssl

import socket

import requests
## Subdomain Enumeration and HTTP Response Capture 

This section describes,

def subdomainEnum_httpResponse(url):

tldextact extracts the domain from the given URL and searched through a list of popular subdomain keywords (source : https://github.com/rbsec/dnscan/blob/master/subdomains-10000.txt)

dns.resolver tries to connect to the generated subdomain URL. If it exists, an HTTP request is made to capture its respnse and get its status code and message.
 
## SSL Certification Check

This section describes,

def sslCheck(url):

Using the 'ssl' module, it creates a connection with the given 'url' using port number: 443. If the connection is establised, certificate's ownner is extracted from the dictonary obtained using '.getpeercert()' from the connection. If the connection is not establised or TimesOut, then the URL does not have a SSL Certificate. 
## Port Scanner

This section describes,

def portScanner(url):

First, IPv4 of the given 'url' is stored usind the 'socket.gethostbyname'. nmap is used to scan through port no. 1 to 250. The result is a dictionary containing
several information we only need check if the port is opened or closed so we will access only that information in the dictionary.
## X-XSS Protection header check

This section describes,

def isXSSHeader(url):

An HTTP is made to the given 'url' using 'requests.get()' from the 'requests' library. 'X-XSS-Protection' is extracted from the 'headers' dictonary from '.get' response.


