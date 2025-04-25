def get_num_words(path) -> int:
    file_content = ""
    with open(path) as f:
        file_content = f.read()
    a = file_content.split()
    return len(a)
def get_num_chars(path) -> int:
    file_content = ""
    with open(path) as f:
        file_content = f.read()
    file_content = file_content.lower()
    dictionary = {}
    for i in file_content:
        if(i not in dictionary):
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    chacracter_count = []
    for char in dictionary:
        if char.isalpha():
            num = dictionary[char]
            chacracter_count.append((char, num))
    chacracter_count.sort(reverse=True, key=lambda x: x[1])
    for x,y in chacracter_count:
        print(f"{x}: {y}")
    