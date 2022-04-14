import requests
from bs4 import BeautifulSoup as BeautifulSoup
import urllib
# soup = BeautifulSoup (html_doc, 'html.parser')
comps = []

def parse(url='https://pdf.11klasov.net/page/1/'):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.content , 'html.parser')
    items = soup.findAll('a', class_='th-in')
    items2 = soup.findAll('div', class_='th-title')
    # print(soup.get_text(url))
    for i in range(len(items)):
        comps.append((items2[i].get_text(), items[i]['href']))


def query(text):
    result=[]
    for item in comps:
        if text.lower() in item[0].lower():
            result.append(item)
    return result

parse()
print(query("математик"))


# for i in range(1, 500):
#     parse(f'https://pdf.11klasov.net/page/{i}/')
#     if i % 10:
#         print(i)




# for i in comps:
#      if  in str(i[0]):
#          i[0] = str(i[0]).replace("</div" , "<div")
#          i[0] = BeautifulSoup(i[0], 'html.parser')

# @bot.message_handler(regexp='Рыбы')
# def handle_message(message):

#         print (comps)


# bot.polling(none_stop=True)