from requests_html import HTMLSession 
from bs4 import BeautifulSoup as bs # importing BeautifulSoup


# sample youtube video url
video_url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
# init an HTML Session
session = HTMLSession()
# get the html content
response = session.get(video_url)
# execute Java-script
response.html.render(sleep=1)
# create bs object to parse HTML
soup = bs(response.html.html, "html.parser")

def get_video_info(url):
    # download HTML code
    response = session.get(url)
    # execute Javascript
    response.html.render(sleep=1)
    # create beautiful soup object to parse HTML
    soup = bs(response.html.html, "html.parser")
    # open("index.html", "w").write(response.html.html)
    # initialize the result
    result["date_published"] = soup.find("meta", itemprop="datePublished")['content']


#get_video_info(video_url)
soup.find("meta", itemprop="name")["content"]


#result["title"] = soup.find("meta", itemprop="name")['content']
