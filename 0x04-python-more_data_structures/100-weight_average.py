#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0
    score_t = 0
    wt_t = 0
    for tupl in my_list:
        score_t += tupl[0] * tupl[1]
        wt_t += tupl[1]
    return score_t / wt_t
