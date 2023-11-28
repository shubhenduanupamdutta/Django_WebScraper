from django.shortcuts import redirect, render
import requests
from bs4 import BeautifulSoup
from .models import Link

# Create your views here.


def scraping(request):
    if request.method == "POST":
        site = request.POST.get('site_url')
        response = requests.get(site)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)

        return redirect('scraping')
    else:
        data = Link.objects.all()

    return render(request, 'scraper/scrape.html', {'data': data})


def clear(request):
    Link.objects.all().delete()
    return redirect(request, 'scraping')
