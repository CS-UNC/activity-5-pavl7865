def more_than_20(file):
    open_file = open(file)
    ret_list = []
    for i in open_file:
        x = i.strip()
        if len(x) > 20:
            ret_list.append(x)
    return ret_list

print(more_than_20('CROSSWD.txt'))

#Function 2

def has_no_e(word):
    return "e" not in word
print(has_no_e('Alex'))
print(has_no_e('Max'))

#Function 3

def uses_only(words, letters):
    for letter in word:
        if letter not in
        letters:
            return False
    return True
print(uses only('Alex')
      

#Function 4

def all_uses_only(file, letters):
    with open(file, 'r') as f:
        words = f.read().split()

    result = []
    for word in words:
        if all(c.lower() in letters.lower() for c in word):
            result.append(word)

    return result