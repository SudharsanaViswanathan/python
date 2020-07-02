from bs4 import BeautifulSoup
import urllib.request as urllib2
for offset in range(0, 10, 10):
    redditFile = urllib2.urlopen(
        "https://www.indeed.com/jobs?q=sql&l=United+States&sort=date&radius=25&start="+str(offset))
    redditHtml = redditFile.read()
    redditFile.close()

    soup = BeautifulSoup(redditHtml, 'html.parser')
    # print(soup)
    jobs = soup.find_all("div",  {"class": "jobsearch-SerpJobCard"})

    # print(jobs)

    #Title = soup.find_all("a",  {"class": "jobtitle turnstileLink","data-tn-element": "jobTitle"})
    #Company = soup.find_all("a",  {"data-tn-element": "companyName"})
    for job in jobs:
        try:
            key = ['title', 'company', 'star', 'date']
            value = [job.find("a",  {"class": "jobtitle turnstileLink", "data-tn-element": "jobTitle"}
                              ).text.strip(), job.find("a",  {"data-tn-element": "companyName"}).text.strip(), job.find("span",  {"class": "ratingsContent"}).text.strip(), job.find("span", {"class": "date"}).text.strip()]
    # Create a zip object from two lists
            dicobj = zip(key, value)
    # Create a dictionary from zip object
            dictOfWords = dict(dicobj)
            print(dictOfWords)
        except:
            try:
                print(job.find("a",  {"class": "jobtitle turnstileLink", "data-tn-element": "jobTitle"}
                               ).text.strip(), job.find("span", {"class": "company"}).text.strip(), job.find("span",  {"class": "ratingsContent"}).text.strip(), job.find("span", {"class": "date"}).text.strip())
            except:
                print(job.find("a",  {"class": "jobtitle turnstileLink", "data-tn-element": "jobTitle"}
                               ).text.strip(), job.find("span", {"class": "company"}).text.strip(), job.find("span", {"class": "date"}).text.strip())
