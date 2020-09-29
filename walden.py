path='C:/Users/sililili/Desktop/Walden.txt'
with open(path,'r') as text:
    words = text.read().split()
    print(words)
    for word in words:
        print('{}--{} times'.format(word,words.count(word)))