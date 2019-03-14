"""This code scraps IPO data from IPOboutique"""

# from util import send_email
# from email.mime.text import MIMEText

from lxml import html
import requests
from bs4 import BeautifulSoup


class IPOboutique_values_getter:

    def __init__(self, url='https://www.ipoboutique.com/cgi/ipo-trackrecord-all-2019.php'):
        self.url = url

    def __str__(self):
        print('This let you find IPO values')

    def get_soup(self, url):
        page = requests.get(url)
        # Create a BeautifulSoup object
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    # get html resources
    def get_tree(self, url=''):
        page = requests.get(url)
        tree = html.fromstring(page.content)
        return tree

    # get links
    def get_links(self):
        soup = self.get_soup(self.url)
        table = soup.find("table")
        links = table.findAll('a')
        new_links = []
        for link in links:
            new_links.append('https://www.ipoboutique.com' + link.get('href'))
        return new_links

    # go to each links and get values from table
    def get_values(self, links):
        json = {}
        for link in links:
            print(f'Working on...{link}')
            soup = self.get_soup(link)
            table = soup.find("table")
            values_array = []
            for line in table.findAll('tr'):
                for l in line.findAll('td'):
                    values_array.append(l.getText())
            dic = {
                    'price_range': values_array[9],
                    'issue_price': values_array[10],
                    'open_price': values_array[11],
                    'IPO_date': values_array[13],
                    }
            json[values_array[8]] = dic
        return json

    def main_code(self):
        links = self.get_links()
        json = self.get_values(links)
        return json

        # Puzzle...
        # Yo Kevin, This Code works, there are so many thing you can improve on this code.
        # Start from printing/saving the result























if __name__ == "__main__":
    IPOboutique_values_getter(url='https://www.ipoboutique.com/cgi/ipo-trackrecord-all-2018.php').main_code()