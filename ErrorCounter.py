import re
from functools import reduce


def count_errors(doc):
    normalized_doc = ''.join(c.lower() if c.isalpha() else '' for c in doc)
    frequencies = {}
    for word in normalized_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def combine_count(d1, d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d


error_doc = r'C:\Users\afournier\PycharmProjects\PythonBeyondBasics\errors.txt'
error_list = []

with open(error_doc) as reader:
    for line in reader.readlines():
        if re.match('([0-9]*-[0-9]*-[0-9]*)', line):
            error_list.append(line)
        else:
            continue




counts = map(count_errors, error_list)

total_counts = reduce(combine_count,counts)
print(total_counts)
