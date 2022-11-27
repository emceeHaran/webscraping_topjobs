from bs4 import BeautifulSoup
import requests
import time


def find_jobs():
    scraping_link = requests.get('http://topjobs.lk/applicant/vacancybyfunctionalarea.jsp?FA=AV').text
    soup = BeautifulSoup(scraping_link, 'html.parser')
    jobs = soup.find_all('h2')
    for job in jobs:
        postion = job.text
        relevant = 'Data'
        new_list = []
        if relevant in postion:
            new_list.append(postion)
            print(new_list)

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 60
        print(f"Waiting {time_wait} seconds.....")
        time.sleep(time_wait)
        

