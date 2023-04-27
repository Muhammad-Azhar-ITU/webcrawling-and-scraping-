# webcrawling-and-scraping-
Web crawling with python Scrapy and scraping with python BeautifulSoap library


Web crawling means to get all urls of a website from a given base url. While web scraping means to extract data from a given URL. There are a number of libraries to do this job. Here we are using python 'Scrapy' for crawling and python "BeautifulSoap" for scraping.


*******************************************************************************************************************************************************************
Web crawling using scrapy.
*******************************************************************************************************************************************************************
Crawling starts a from a base URL for example "https://www.example.com", find all URLs in this URL page, store in a list and repeat the same for all discovered URLs which starts from the given domain. Follow following instructions to crawl a website. Remember to install scrapy package in the environment first.

Step#1: create scrapy project where you want to work. Do it GUI based or navigate to directory using command line interface, using following command: 
"scrapy startproject project_name"
It will create a drectory with name 'project_name'. You can chose any name.

Step#2: Use command line interface and navigate to the project_name directory.

Step#3: Create a scrapy spider using below command:
"scrapy genspider -t crawl my_spider https://www.example.com/"
Edit "https://www.example.com/" with the URL you want to crawl. You can also replace my_spider with the name you want to give to your spider.

Step#4: After running this command, few files and folders will be created in your project directory. There will a spider file by in project_name/project_name/spiders/my-spider, you will also get instruction in cmd when you run the above command. This spider file is actually the file you need to modify according to your need. 

Step#5: Copy the code from my repository file "my_spider.py" and paste in the my_spider file, except bellow two lines: 
    allowed_domains = ["www.example.com"]
    start_urls = ["http://www.example.com/"]
Because these lines sets the base URL which you mentioned while creating the project.

Step#6: Save the file and run following command. 
"scrapy crawl my_spider -o output.csv"
It will take some time according to the internet speed, server response and website complexity. Finally a file name "output.csv" will be created in the directory where spider code is located. This file contained all URLs which starts from base address you given.

open and see the "output.csv" file. it may contains soome unnecessary URLs, you can remove them using python script. You can extract list of URLs for specific domain, for example if you want to extarct faculty data of university you can make a script that extract data whick match "http://www.example.com/faculty".

*******************************************************************************************************************************************************************
Web scraping with BeautifulSoap
*******************************************************************************************************************************************************************
In web scraping, we give a URL and list of URLS and extract data. We can extract data from ech HTML element. In my script we simply extracting the all textual data from a list of URLs. Install bs4 package and follow these instructions.

Step#1: Download "Web_Scraping.ipynb" from this repository. Put it in the directory where spider file and output.csv is located. Here the "output.csv" in the code is the file which contains crawled URLs from our spider. You can also give other list of URLs. Open and run it.
It will take sometime according to the internet speed, server response and website complexity, once run finish, a file "extracted_data.csv" will be created that have extraced all data from URLs in the file "output.csv".

Note that you can also give one URL or a few URLs which you want to extarct data.
*******************************************************************************************************************************************************************

*******************************************************************************************************************************************************************

