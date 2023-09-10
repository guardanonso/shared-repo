import requests
from bs4 import BeautifulSoup

url = input("Type in an url: ")

html = requests.get(url)

soup = BeautifulSoup(html.content,"html.parser")

result = soup.find(id="ResultsContainer")

job_elements = result.find_all("div", class_="card-content")

for job_element in job_elements:
    print(job_element, end = "\n\n")

# https://www.trony.it/online
# https://realpython.github.io/fake-jobs/