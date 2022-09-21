# -*- coding: utf-8 -*-
"""
@author: Vindhyaa Saravanan

FAKE PYTHON JOBS SITE SCRAPER

Objective: To scrape data from the fake Python jobs site, clean up and parse 
it, and save the data for further usage in a csv file.
"""

# IMPORTING REQUIRED MODULES
import requests
from bs4 import BeautifulSoup
import csv

# To get the page content from url and parse the structured data
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# To get list of job results
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")


# OPENING A FILE TO WRITE CLEAN DATA
csvfile = open("jobs.csv", "w", newline='')
writer = csv.writer(csvfile)

# Write header to the file
header = ['Serial No.','Job Title', 'Company', 'Location']
writer.writerow(header)

job_number = 1

# WRITING DATA TO FILE
# To get the pertinent information from each job result
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    
    new_job = []
    new_job.append(job_number)
    new_job.append(title_element.text)
    new_job.append(company_element.text)
    new_job.append(location_element.text)
    
    writer.writerow(new_job)
    job_number = job_number + 1
    
csvfile.close()


