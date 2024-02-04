#(1)
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

#(2)
import datetime
class bk:
    def __init__(self, id=None, title=None):
        self.id = id
        self.title = title

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def set_id(self, value):
        self.__id = value

    def set_title(self, value):
        self.__title = value

def csv_loader(name):
    import pandas as pd
    try:
        df = pd.read_csv('/Users/Ted/Desktop/computer_science/INFS3200/assignment/dataset/{}.csv'.format(name),header=None)
    except:
        try:
            df = pd.read_csv('../dataset/{}.csv'.format(name),header=None)
        except:
            print('no file.')
            return
    books=[]
    for i in range(len(df)):
        book=bk()
        book.set_id(df[0].values[i])
        book.set_title(str(df[1].values[i]))
        books.append(book)
    return books

def calc_measure(results):
    try:
        try:
            with open('/Users/Ted/Desktop/computer_science/INFS3200/assignment/dataset/Book1and2_pair.csv', 'r') as f:
                benchmark = f.read().splitlines()
        except:
            with open('../dataset/Book1and2_pair.csv', 'r') as f:
                benchmark = f.read().splitlines()
        if benchmark is None:
            print("no file.")
    except:
        print("Error occurred. Check if file exists")
    if len(results) == 0:
        print('Precision = 0, Recall = 0, Fmeasure = 0')
        return
    count = 0
    for pair in results:
        if pair in benchmark:
            count = count + 1
    if count == 0:
        print('Precision=0, Recall=0, Fmeasure=0')
        return
    precision = count / len(results)
    recall = count / len(benchmark)
    f_measure = 2 * precision * recall / (precision + recall)
    print("Precision=", precision, ", Recall=", recall, ", Fmeasure=", f_measure)
    return

def nested_loop_by_title_jaccard(threshold, q):
    books1 = csv_loader('Book1')
    books2 = csv_loader('Book2')
    results = []
    book1 = bk()
    book2 = bk()
    id1 = 0
    id2 = 0
    title1 = None
    title2 = None
    start_time = datetime.datetime.now()
    for i in range(0, len(books1)):
        book1 = books1[i]
        id1 = book1.get_id()
        title1 = book1.get_title()
        for j in range(0, len(books2)):
            book2 = books2[j]
            id2 = book2.get_id()
            title2 = book2.get_title()
            sim = calc_jaccard(title1, title2, q)
            if sim > threshold:
                results.append(str(id1) + ',' + str(id2))
    end_time = datetime.datetime.now()
    time = end_time - start_time
    print("Total Time:", round(time.total_seconds() * 1000, 3), 'milliseconds')
    calc_measure(results)



#(1)
str1 = "Richmond Shee, Kirtikumar Deshpande and K. Gopalakrishnan;" 
str2 = "K. Gopalakrishnan, Kirtikumar Deshpande, and Richmond Shee" 
out = calc_ed_sim(str1, str2) 
print("Edit Distance =", out)
out1 = calc_jaccard(str1, str2, 1) 
print("Jaccard Coefficient with 1-gram =", out1)
out2 = calc_jaccard(str1, str2, 2) 
print("Jaccard Coefficient with 2-gram =", out2)
out3 = calc_jaccard(str1, str2, 3) 
print("Jaccard Coefficient with 3-gram =", out3)
print('-'*50)



#(2)
nested_loop_by_title_jaccard(0.75, 3)
