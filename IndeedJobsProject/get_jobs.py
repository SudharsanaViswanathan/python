
#Web Scraping
from bs4 import BeautifulSoup
import urllib.request as urllib2

#cosmos db clients
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import azure.cosmos.http_constants as http_constants
from azure.cosmos.partition_key import PartitionKey
from constants import *

#Initialising client
client = cosmos_client.CosmosClient(url, {'masterKey': key})
database = client.get_database_client(database_id)
container_client = database.get_container_client(container_id)

for offset in range(0, 3000, 10):
    redditFile = urllib2.urlopen(
        "https://www.indeed.com/jobs?q=sql&l=United+States&sort=date&radius=25&start="+str(offset))
    redditHtml = redditFile.read()
    redditFile.close()

    soup = BeautifulSoup(redditHtml, 'html.parser')

    jobs = soup.find_all("div",  {"class": "jobsearch-SerpJobCard"})

    for count,job in enumerate(jobs, start=1):
        try:
            container_client.upsert_item({'id':str(count),
            'title': job.find("a",  {"class": "jobtitle turnstileLink", "data-tn-element": "jobTitle"}
                              ).text.strip(),'company': job.find("a",  {"data-tn-element": "companyName"}).text.strip(),'rating': job.find("span",  {"class": "ratingsContent"}).text.strip(), 'posted_date':job.find("span", {"class": "date"}).text.strip()})
        except:
            try:
                container_client.upsert_item({'id':str(count),'title':job.find("a",  {"class": "jobtitle turnstileLink", "data-tn-element": "jobTitle"}
                               ).text.strip(),'company': job.find("span", {"class": "company"}).text.strip(),'rating': job.find("span",  {"class": "ratingsContent"}).text.strip(),'posted_date': job.find("span", {"class": "date"}).text.strip()})
            except:
                try:
                    container_client.upsert_item({'id':str(count),'title':job.find("a",  {"class": "jobtitle turnstileLink", "data-tn-element": "jobTitle"}
                               ).text.strip(),'company': job.find("span", {"class": "company"}).text.strip(),'rating':'NA','posted_date': job.find("span", {"class": "date"}).text.strip()})
                except:
                    pass
