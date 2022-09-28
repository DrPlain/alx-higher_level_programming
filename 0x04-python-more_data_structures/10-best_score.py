#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    sorted_list = sorted(a_dictionary.items(),
                         key=lambda item: item[1], reverse=True)
    return sorted_list[0][0]
