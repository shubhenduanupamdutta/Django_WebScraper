from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link

# Create your views here.


def scraping(request):
    response = requests.get('https://www.google.com/')
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a'):
        link_address = link.get('href')
        link_text = link.string
        Link.objects.create(address=link_address, name=link_text)

    data = Link.objects.all()

    return render(request, 'scraper/scrape.html', {'data': data})
