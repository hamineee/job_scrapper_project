import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL =  f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find('div', class_='pagination')
    links = pagination.find_all('a')

    pages = []

    for link in links[:-1] :
        pages.append(int(link.find('span').string))

    max_page = pages[-1]        
    return max_page

def extract_job(html):
    title = html.find('h2', class_='title').find('a')['title']  
    company = html.find('span', class_='company')
    if company:
        company_anchor = company.find('a')
        if company_anchor is not None:
            company = (str(company_anchor.string))
        else:
            company = (str(company.string))
        company = company.strip()
    else:
        company = None
    location = html.find('div', class_='recJobLoc')['data-rc-loc']
    job_id = html["data-jk"]

    return {
        'title': title,
        'company': company,
        'location': location,
        'apply_link': f"https://www.indeed.com/viewjob?jk={job_id}"
        }




def extract_jobs(lastpage):
    jobs = []
    #for page in range(lastpage):
        #print(f"Scrapping page(indeed) {page}")
    result = requests.get(f"{URL}&start={1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all('div', class_='jobsearch-SerpJobCard')
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs

def get_jobs():
    lastpage = extract_pages()
    jobs = extract_jobs(lastpage)
    print (jobs)

get_jobs()
     
    













