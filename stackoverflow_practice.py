import requests
from bs4 import BeautifulSoup


def get_last_page(URL):
    results = requests.get(URL)
    soup = BeautifulSoup(results.text, "html.parser")
    pages = soup.find('div', class_='s-pagination').find_all('span')
    lastpage = pages[-2].string
    return int(lastpage)

def extract_job(html):
    title = html.find('h2').find('a')['title']
    company= html.find('h3', class_='fc-black-700').find('span')
    location= html.find('h3', class_='fc-black-700').find('span', class_='fc-black-500')
    company=company.get_text(strip=True)
    location=location.get_text(strip=True).strip('-').strip('\r').strip('\n')
    return {'title': title, 'company': company, 'location': location}



def extract_jobs(lastpage, URL):
    jobs = []
    for page in range(lastpage):
        print(f"Scrapping page {page+1}")
        result = requests.get(f"{URL}&PG={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all('div', class_='js-result') 
        for result in results:
            job = extract_job(result)
            jobs.append(job) 
    return jobs


def get_jobs(word):
    URL = f"https://stackoverflow.com/jobs?q={word}"
    lastpage = get_last_page(URL)
    jobs = extract_jobs(lastpage, URL)
    print(jobs)

get_jobs('python')


    


 