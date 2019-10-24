from bs4 import BeautifulSoup
import urllib.request

def print_list(l):
    for o in l:
        print(o)
    print()

url = "https://news.google.com/?hl=en-US&gl=US&ceid=US:en"
max_results = 3
keyword = "Trump"

page = urllib.request.urlopen(url)
    
soup = BeautifulSoup(page, 'html.parser')
# print(soup)

print(type(soup))

headlines = soup.find_all('h3')
print_list(headlines)

trump_headlines = []
for headline in headlines:
    if keyword in headline.getText():
        trump_headlines.append(headline.getText())
print_list(trump_headlines)

print_list(trump_headlines[:max_results])
