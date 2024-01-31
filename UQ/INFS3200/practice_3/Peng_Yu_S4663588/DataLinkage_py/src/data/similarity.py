'''
Created on 1 May 2020

@author: shree
'''


def calc_jaccard(str1, str2, q):
    str1_tokens = tokenize(str1, q)
    str2_tokens = tokenize(str2, q)
    total_tokens = str1_tokens + str2_tokens
    total_tokens = list(set(total_tokens))
    return (len(str1_tokens) + len(str2_tokens) - len(total_tokens)) / len(total_tokens)


def tokenize(string, q):
    if q != 0:
        if len(string) < q:
            str_tokens = [string]
        else:
            str_tokens = [string[i:i + q] for i in range(0, len(string) - q + 1, 1)]
        return list(set(str_tokens))
    else:
        str_tokens = string.split(" ")
        return list(set(str_tokens))


def calc_ed_sim(str1, str2):
    if str1 == str2:
        return 1
    ed = calc_ed(str1, str2)

    return 1 - (ed / max(len(str1), len(str2)))


def calc_ed(str1, str2):
    ed = 0

    '''
         * Please implement the calculation of edit distance between two strings
         * Dynamic programming should be used
         */
    '''
    r, l = (len(str1) + 1), (len(str2) + 1)
    edit = [[0] * l for i in range(r)]
    for i in range(1,r):
        edit[i][0] = i
    for j in range(1,l):
        edit[0][j] = j
    for i in range(1,r):
        for j in range(1,l):
            if str1[i-1] == str2[j-1]:
                cost = 0
            else:
                cost = 1 
            edit[i][j] = min((edit[i-1][j] + 1), (edit[i][j-1] + 1), (edit[i-1][j-1] + cost))
    ed = edit[r-1][l-1]
    return ed

str1 = "University Queensland" 
str2 = "Queensland University" 
out = calc_ed(str1, str2) 
print("Edit Distance = ", out)
out1 = calc_ed_sim(str1, str2) 
print("Edit Distance Similarity = ", out1)
out2 = calc_jaccard(str1, str2, 2) 
print("Jaccard Coefficient = ", out2)
