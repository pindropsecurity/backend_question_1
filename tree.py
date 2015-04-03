import tokenize, token

print 'Hello World'

class tree:
    def __init__(self, inStr):
        for t in tokenize.generate_tokens(iter([inStr]).next):
            print token.tok_name[t[0]],
        print

t = tree('[+ [1 2]]')
print 'Bye-bye World'
