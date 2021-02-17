import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#print(data)
import bs4 
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="title")
print(titles)
#for t in titles:
    #if titles.a !=None:  
     #   print(titles)
