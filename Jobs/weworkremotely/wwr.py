
from requests import get 
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword) :
    base_url = " https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term= "

    response = get(f"{base_url}{keyword}")

    if response.status_code != 200 :
        print("Can't request website!")
    else :
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("section", class_="jobs")

        for job_section in jobs:
            job_posts = job_section.find_all('li')
            job_posts.pop(-1)
            
            for post in job_posts:
                anchors = post.find_all("a")
                anchor = anchors[1]
                link = anchor['href']
                company, kind, region = anchor.find_all('span', class_="company")
                
                title = anchor.find('span', class_='title')
                # print(company.string, kind.string, region.string, title.string)
                
                job_data = {
                    'link' : f"https://weworkremotely.com{link}", 
                    'company' : company.string,
                    'region' : region.string,
                    'position' : title.string
                }         
        
                results.append(job_data)
                
    return results

