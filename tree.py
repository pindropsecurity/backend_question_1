import tokenize 
import io
import StringIO
import sys

class tree:
    def __init__(self, inStr):
        for toktyp, toksym, _, _, _ in tokenize.generate_tokens(iter([inStr]).next):
            if toktyp == tokenize.NUMBER:
                print 'THIS IS A NUMBER'
            elif toktyp == tokenize.OP and '[' in toksym:
                print 'THIS IS A ['
            elif toktyp == tokenize.OP and ']' in toksym:
                print 'THIS IS A ]'
            elif toktyp == tokenize.OP and '+' in toksym:
                print 'THIS IS A +'
            elif toktyp == tokenize.OP and '-' in toksym:
                print 'THIS IS A -'
            elif toktyp == tokenize.OP and '*' in toksym:
                print 'THIS IS A *'
            elif toktyp == tokenize.OP and '/' in toksym:
                print 'THIS IS A /'
            elif toktyp == tokenize.ENDMARKER:
                print 'THE END'
            else:
                print 'THIS IS A SPLAT'

        src = StringIO.StringIO(iter([inStr]).next)
        #print toktyp
        #tokenize.generate_tokens(StringIO(inStr).readline);


#t = tree('[+[1 2 [- 3 2]]]')
t = '[+[1 2 [- 3 2]]]'

tokenizer = tokenize.generate_tokens(iter([t]).next)
print type(tokenizer)
top = tokenizer.next()
print top
top = tokenizer.next()
print top
print 'Bye-bye World'
