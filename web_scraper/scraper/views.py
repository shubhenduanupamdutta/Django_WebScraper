from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.


def scraping(request):
    response = requests.get('https://www.google.com/')
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    all_links = []
    for link in soup.find_all('a'):
        all_links.append(link.get('href'))

    return render(request, 'scraper/scrape.html', {"links": all_links})
