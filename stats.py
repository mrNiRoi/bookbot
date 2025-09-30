def get_num_words(content):
    all_words = content.split()
    num_words = len(all_words)
    return num_words

def get_num_char(text):
    char_num_dict = {}

    for char in text:
        c = char.lower()
        if c not in char_num_dict:
            char_num_dict[c] = 1
        else:
            char_num_dict[c] += 1
    return char_num_dict

    
def sort_on(items):
    return items["num"]

def sort_dict(dict):
    last_list = []

    for key in dict:
        temp_dict = {
            "char": key,
            "num": dict[key],
        }
        last_list.append(temp_dict)
    
    last_list.sort(reverse=True, key=sort_on)
    return last_list



