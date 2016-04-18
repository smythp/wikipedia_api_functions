from connect import get_infobox_category_from_search


while 1:
    input = raw_input('Which title? ')
    if input=='exit':
        break
    out = get_infobox_category_from_search(input,'Publication date')
    if out:
        print(out)
    else:
        print('No data fond for that search...')
    
