import tokenize, token

print 'Hello World'

class tree:
    def __init__(self, inStr):
        for toktyp, toksym, _, _, _ in tokenize.generate_tokens(iter([inStr]).next):
            if toktyp == tokenize.NUMBER:
                print 'THIS IS A NUMBER'
            elif toktyp == tokenize.OP and '[' in toksym:
                print 'THIS IS A ['
            elif toktyp == tokenize.OP and ']' in toksym:
                print 'THIS IS A ]'
            elif toktyp == tokenize.ENDMARKER:
                print 'THE END'
            else:
                print 'THIS IS A SPLAT'
        print

t = tree('[+ [1 2]]')
print 'Bye-bye World'
