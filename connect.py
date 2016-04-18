from bs4 import BeautifulSoup
import urllib2

from wikiapi import WikiApi
wiki = WikiApi()
wiki = WikiApi({ 'locale' : 'en'})

# b = wiki.get_article('High Crusade')

# print(b.url)


#results = wiki.find('Barack Obama').content

#print(results)

def get_title_from_search(string):
    return wiki.find(string)[0]
    

def get_url_from_search(string):
    article_title = wiki.find(string)[0]
    article_contents = wiki.get_article(article_title)
    return article_contents.url


# print(get_url_from_search('Stranger in a Strange Land'))

def get_infobox_from_url(url):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url,headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page.read(),'lxml')
    table = soup.find('table', class_='infobox vcard')
    if table == None:
        return False
    result = {}
    exceptional_row_count = 0

    for tr in table.find_all('tr'):
        if tr.find('th'):
            key_gen = tr.find('th').text.rstrip().lstrip()
            result[key_gen] = tr.find('td').text
        else:
            # the first row Logos fall here
            exceptional_row_count += 1
    if exceptional_row_count > 1:
        print 'WARNING ExceptionalRow>1: ', table
    return result

def get_infobox_from_search_string(string):
    url = get_url_from_search(string)
    return get_infobox_from_url(url)
        
# get a category like 'Publication date'    
def get_infobox_category_from_url(url,category):
    category_dict = get_infobox_from_url(url)
    print(category_dict)
    if category_dict:
        return category_dict[category]

# Return infobox result from search string and desired category
def get_infobox_category_from_search(string,category):
    try: 
        category_dict = get_infobox_from_search_string(string)
        if category_dict:
            return category_dict[category]
        else:
            return False
    except KeyError:
        return False

# print(get_infobox_category_from_search('Stranger in a Strange Land','Publication date'))

# print(get_infobox_from_search_string('Stranger in a Strange Land'))

# print(get_title_from_search('1984 (novel)'))

# print(get_url_from_search('1984 (novel)'))
