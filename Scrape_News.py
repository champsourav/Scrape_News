from bs4 import BeautifulSoup
import requests
res=requests.get('https://www.indiatoday.in/')
soup=BeautifulSoup(res.text,'lxml')
print("Choose the category \n \n --Latest news(choose 1)\n --Business(choose 2) \n ")
num=int(input("Enter Choice: "))
if num==1:
    print()
    news_box=soup.find('ul',{'class':'itg-listing'})
    all_news=news_box.find_all('a')
    q=1
    for news in all_news:
        print(q,news.text)
        q+=1
if num==2:
    print()
    news_box=soup.find('div',{'class':'section-ordering video-gif'})
    all_news=news_box.find_all('a')
    q=0
    for news in all_news:
        if q<=3:
            print(q,news.text)
            q+=1

