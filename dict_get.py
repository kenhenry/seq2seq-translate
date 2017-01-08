words = {'a': 1, 'b': 2, 'c': 3}
b_word = [b'a', b'b', b'c']
type(words)
type(b_word)
print(words)
print(b_word)
x =str(b'a')
y = b'a'.decode()
get_word = words.get((x),'null')
print(get_word)
get_word = words.get((y),'null')
print(x)
print(y)
print(get_word)