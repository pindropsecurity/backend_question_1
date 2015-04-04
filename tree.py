import tokenize 

operators = ['+', '-', '*', '/']

def operate(op, val1, val2):
    if (op == '+'):
        return val1 + val2
    elif (op == '-'):
        return val1 - val2
    elif (op == '*'):
        return val1 * val2
    elif (op == '/'):
        return val1 / val2
    else:
       assert False, 'Lost all hope'


def reduce(tokenizer):

    toktyp,tokval, _,_,_ = tokenizer.next()

    if toktyp == tokenize.OP and any(s in tokval for s in operators):

        #
        # Enforce the fact that every node has at least 2 children
        #
        print 'OP ' + tokval
        accum = reduce(tokenizer)  
        print 'accum1 ' + str(accum)

        try:
            accum = operate(tokval, accum, reduce(tokenizer))
        except StopIteration:
            print 'Node must be >= 2'
            raise StopIteration

        print 'accum2 ' + str(accum)
 
        #
        # Manage the case for > 2
        #
        while True:
            try:
                print 'accum3 ' + str(accum)
                accum = operate(tokval, accum, reduce(tokenizer))
            except StopIteration:
                return accum
            except EOFError:
                return accum

    elif toktyp == tokenize.NUMBER:
        print "Habemus NUMBER " + tokval
        return int(tokval)
    elif toktyp == tokenize.ENDMARKER:
        print "Habemus ENDMARKER "
        raise EOFError
    else:
        print "Habemus splat"
        raise SyntaxError

def tree (t):
    tokenizer = tokenize.generate_tokens(iter([t]).next)
    result = reduce(tokenizer)
    tokenizer.close()
    return result

#tree('+ + 1 2 + 3 4')
tree('+ + + 1 2 3')
#tree('+ + 1 2 + 3 4')
