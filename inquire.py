from connect import get_infobox_category_from_search,get_infobox_from_search_string

def lookup_book(input,tried_disambiguation=False):

    out = get_infobox_from_search_string(input)

    if out:
        if 'Publication date' in out:
            return out['Publication date']
        if 'Published' in out:
            return out['Published']
    else:
        if tried_disambiguation:
            return 'No data found for that search...'
        else:
            return lookup_book(input+' (novel)',tried_disambiguation=True)
        


while 1:
    input = raw_input('Which title? ')
    print(lookup_book(input))

    
