KadirTugcuCrawler-X
--
The purpose of the submission is to transfer Kadir Tuğcu's documents about child health to a database.

## How to Use ?
1) Create a scrapy project(project_name = kadir_tugcu):  
`scrapy startproject project_name`  

2) Enable virtual enviroment:  
`source kadir_tugcu/env/bin/activate`  
  
3) Install project requirements(Make sure that the text (env) is displayed before you do the uploads.):  
`pip install -r requirements.txt`  

4) Change the MySQL information to match your system.(If you are using a lamp and do not need it, you can delete the 'socket' line.)(in pipelines.py)  

5) Now, you are ready, start spider!
`scrapy crawl KadirTugcuScraper`
