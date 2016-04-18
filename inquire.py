from connect import get_infobox_category_from_search,get_infobox_from_search_string


while 1:
    input = raw_input('Which title? ')
    if input=='exit':
        break
    out = get_infobox_from_search_string(input)
#    print(out)
    if out:
        if 'Publication date' in out:
            print(out['Publication date'])
        if 'Published' in out:
            print(out['Published'])
    else:
        print('No data found for that search...')
    
