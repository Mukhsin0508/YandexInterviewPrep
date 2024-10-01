def remove_duplicates(words: str):

    list1 = [ ]
    for word in words.split():
        if word not in list1:
            list1.append((word))
    return ' '.join(list1)

print(remove_duplicates("Hello Hello World World"))