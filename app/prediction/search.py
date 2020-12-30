import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse

def get_links(url, param):
    cleaned_links = set()
    try:
        html = requests.get(url)
        if html.status_code==200:
            soup = BeautifulSoup(html.text, 'lxml')
            anchor_list = soup.find_all('a')
            for i in anchor_list:
                links = i.get('href')
                try:
                    m = re.search("(?P<url>https?://[^\s]+)", links)
                    n = m.group(0)
                    rul = n.split('&')[0]
                    domain = urlparse(rul)
                    if(re.search('google.com', domain.netloc)):
                        continue
                    else:
                        if param == 'g' and not rul.startswith('https://www.youtube.com'):
                            cleaned_links.add(rul)
                        elif param == 'y' and rul.startswith('https://www.youtube.com') and not rul.startswith('https://www.youtube.com/watch%'):
                            cleaned_links.add(rul)
                        else:
                            continue
                except:
                    continue
    except Exception as ex:
        print(str(ex))
    finally:
        return cleaned_links;

def search(query):
    google_search = []
    youtube_search = []
    google_url = 'https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8'.format(query+' recipe')
    youtube_url = 'https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8'.format(query+' recipe youtube')
    google_search = get_links(google_url, 'g')
    youtube_search = get_links(youtube_url, 'y')
    return google_search, youtube_search

# foods = ['apple pie'
# ,'baby back ribs'
# ,'baklava'
# ,'beef carpaccio'
# ,'beef tartare'
# ,'beet salad'
# ,'beignets'
# ,'bibimbap'
# ,'bread pudding'
# ,'breakfast burrito'
# ,'bruschetta'
# ,'caesar salad'
# ,'cannoli'
# ,'caprese salad'
# ,'carrot cake'
# ,'ceviche'
# ,'cheese plate'
# ,'cheesecake'
# ,'chicken curry'
# ,'chicken quesadilla'
# ,'chicken wings'
# ,'chocolate cake'
# ,'chocolate mousse'
# ,'churros'
# ,'clam chowder'
# ,'club sandwich'
# ,'crab cakes'
# ,'creme brulee'
# ,'croque madame'
# ,'cup cakes'
# ,'deviled eggs'
# ,'donuts'
# ,'dumplings'
# ,'edamame'
# ,'eggs benedict'
# ,'escargots'
# ,'falafel'
# ,'filet mignon'
# ,'fish and chips'
# ,'foie gras'
# ,'french fries'
# ,'french onion soup'
# ,'french toast'
# ,'fried calamari'
# ,'fried rice'
# ,'frozen yogurt'
# ,'garlic bread'
# ,'gnocchi'
# ,'greek salad'
# ,'grilled cheese sandwich'
# ,'grilled salmon'
# ,'guacamole'
# ,'gyoza'
# ,'hamburger'
# ,'hot and sour soup'
# ,'hot dog'
# ,'huevos rancheros'
# ,'hummus'
# ,'ice cream'
# ,'lasagna'
# ,'lobster bisque'
# ,'lobster roll sandwich'
# ,'macaroni and cheese'
# ,'macarons'
# ,'miso soup'
# ,'mussels'
# ,'nachos'
# ,'omelette'
# ,'onion rings'
# ,'oysters'
# ,'pad thai'
# ,'paella'
# ,'pancakes'
# ,'panna cotta'
# ,'peking duck'
# ,'pho'
# ,'pizza'
# ,'pork chop'
# ,'poutine'
# ,'prime rib'
# ,'pulled pork sandwich'
# ,'ramen'
# ,'ravioli'
# ,'red velvet cake'
# ,'risotto'
# ,'samosa'
# ,'sashimi'
# ,'scallops'
# ,'seaweed salad'
# ,'shrimp and grits'
# ,'spaghetti bolognese'
# ,'spaghetti carbonara'
# ,'spring rolls'
# ,'steak'
# ,'strawberry shortcake'
# ,'sushi'
# ,'tacos'
# ,'takoyaki'
# ,'tiramisu'
# ,'tuna tartare'
# ,'waffles']

# for food in foods1:
#     arr1, arr2 = search(food)
#     arr1_str = '\n'.join([str(elem) for elem in arr1])
#     arr2_str = '\n'.join([str(elem) for elem in arr2])
#     f = open("demo.txt", "a")
#     f.write(arr1_str);
#     f.write(arr2_str);
#     f.write("\n----Line break----\n")
#     f.close()
