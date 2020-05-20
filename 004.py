import re


sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations \
Might Also Sign Peace Security Clause. Arthur King Can."
heads = {1, 5, 6, 7, 8, 9, 15, 16, 19}
d = {}
splited_sentence = re.sub("[^a-zA-z]", " ", sentence).split()
d = {(splited_sentence[i][0] if i + 1 in heads else splited_sentence[i]
      [:2]): i + 1 for i in range(len(splited_sentence))}
print(d)
