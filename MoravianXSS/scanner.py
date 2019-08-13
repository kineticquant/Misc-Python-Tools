#MM 08.12.2019

####                       ####      ####                       ####
####  ###             ###  ####      ####  ###             ###  ####
####     ###      ###      ####      ####     ###      ###      ####
####        ## ##          ####      ####        ## ##          ####
####          #            ####      ####          #            ####
####                       ####      ####                       ####
####                       ####      ####                       ####
####                       ####      ####                       ####
####                       ####      ####                       ####

import requests
import re
import urlparse
from BeautifulSoup import BeautifulSoup

class Scanner:
    def __init__(self, url, ignore_links):
        #Authentication protocol to open, maintain, and close session.
        self.session = requests.Session()
        self.target_url = url
        self.target_links = []
        self.links_to_ignore = ignore_links

    def extract_links_from(self, url):
        response = self.session.get(url)
        return re.findall('(?:href=")(.*?)"', response.content)

    #None default parameter allows me to call method without specifying a URL.
    def crawl(self, url=None):
        #Check if method called from outside of class.
        if url == None:
            url = self.target_url
        href_links = self.extract_links_from(url)
        for link in href_links:
            link = urlparse.urljoin(url, link)

            if "#" in link:
                link = link.split("#")[0]
            #Make sure we ignore links below whenever they are in the ignore list.
            if self.target_url in link and link not in self.target_links and link not in self.links_to_ignore:
                self.target_links.append(link)
                print(link)
                #Recursive call.
                self.crawl(link)

    def extract_forms(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content)
        #Can either store this in a variable or return it.
        return parsed_html.finaAll("form")
        #forms_list = parsed_html.findAll("form")

    def submit_form(self, form, value, url):
        #Extract action and joins to URL to get passed to method.
        action = form.get("action")
        post_url = urlparse.urljoin(url, action)
        method = form.get("method")

        inputs_list = form.findAll("input")
        post_data = {}
        #Iterating over inputs.
        for input in inputs_list:
            input_name = input.get("name")
            input_type = input.get("type")
            input_value = input.get("value")
            if input_type == "text":
                input_value = value
            #NOTE: Most forms use POST but not all - Some use GET Methods!
            post_data[input_name] = input_value
        if method == "post":
            #Can either store this result in a variable or return it.
            return self.session.post(post_url, data=post_data)
            #results = self.session.post(post_url, data=post_data)
        #References GET method with POST data being passed to params argument instead of data argument.    
        return self.session.get(post_url, params=post_data)