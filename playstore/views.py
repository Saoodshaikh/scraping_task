from urllib import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
import requests
from google_play_scraper import app
from bs4 import BeautifulSoup
import pymongo
from django.conf import settings
import urllib 
from pymongo import MongoClient
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET','POST'])
def scrap(request):
    url="https://play.google.com/store/games"
    params={
        'hl':'en',
        'gl':'US'
    }
    header={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    api=requests.get(url,params=params,headers=header)
    htmlcontent=api.content
    soup=BeautifulSoup(htmlcontent, 'html5lib')
    all_packages=soup.find_all('a',attrs={"class":"Si6A0c"})
    packages_names=[]
    for package in all_packages:
        packages_names.append(package['href'][23:])

    package_detail = []

    for package_name in packages_names:
        result = app(
            package_name,
            lang='en', # defaults to 'en'
            country='us' # defaults to 'us'
        )
        package_detail.append(result)


    client = pymongo.MongoClient('localhost', 27017)
    db = client["testdb"]
    my_collection = db["demo"]
    my_collection.insert_many(package_detail)
    count=count(package_detail)
    return response({"data fatched from google play store":count})
            
