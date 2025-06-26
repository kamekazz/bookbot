def get_num_of_words(_text):
    return len(_text.split())

def count_characters (_data)-> dict[str,int]:
    obj ={}
    for l in _data.lower():
        obj[l] = obj.get(l,0) + 1
    return obj


