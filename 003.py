import re


# 解法1
sentence = "Now I need a drink, alcoholic of course, after the heavy lectures \
involving quantum mechanics."
sentence = sentence.replace(",", "").replace(".", "")
splited = sentence.split()
print([len(word) for word in splited])

# 解法2
sentence = "Now I need a drink, alcoholic of course, after the heavy lectures \
    involving quantum mechanics."
splited = re.sub("[^a-zA-Z]", " ", sentence).split()
print([len(word) for word in splited])
