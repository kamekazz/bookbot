def get_num_of_words(_text):
    return len(_text.split())

def count_characters (_data)-> dict[str,int]:
    objs ={}
    for l in _data.lower():
        objs[l] = objs.get(l,0) + 1
    return objs



def convert_dic_list(objs: dict[str,int]) -> list[dict[str,int]]:
    lst = [{"char": c, "num": n} for c, n in objs.items()]
    lst.sort(key=lambda item: item["num"], reverse=True)
    return lst

def create_dic(_char,_num)-> dict:
    return {"char",_char,"num",_num}