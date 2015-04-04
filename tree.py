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


def reduce(tokenizer, depth):

    childcount = 0
    toktyp,tokval, _,_,_ = tokenizer.next()

    if toktyp == tokenize.OP and any(s in tokval for s in operators):

        print 'OP ' + tokval + ' ' +str(depth)
        accum = reduce(tokenizer, depth+1)  
        childcount += 1
        print 'accum1 ' + str(accum) + ' depth ' + str(depth) + ' childcount ' + str(childcount)

        try:
            accum = operate(tokval, accum, reduce(tokenizer, depth+1))
            childcount += 1
            print 'accum1.5 ' + str(accum) + ' depth ' + str(depth) + ' childcount ' + str(childcount)
        except StopIteration:
            print 'StopIteration depth ' + str(depth)
            if childcount > 1:
                return accum
            else:
                print 'Node must be >= 2'
                raise StopIteration

        print 'accum2 ' + str(accum) + ' depth ' + str(depth) + ' childcount ' + str(childcount)
 
        #
        # Manage the case for > 2
        #
        while True:
            try:
                print 'accum3 ' + str(accum) + ' depth ' + str(depth) + ' childcount ' + str(childcount)
                accum = operate(tokval, accum, reduce(tokenizer, depth+1))
                childcount += 1
            except StopIteration:
                if childcount <= 1:
                    raise StopIteration
                else:
                    return accum
            except EOFError:
                return accum

    elif toktyp == tokenize.NUMBER:
        print "Habemus NUMBER " + tokval + ' depth ' + str(depth)
        return int(tokval)
    elif toktyp == tokenize.ENDMARKER:
        print "Habemus ENDMARKER " + ' depth ' + str(depth)
        raise EOFError
    else:
        print "Habemus splat"
        raise SyntaxError

def tree (t):
    tokenizer = tokenize.generate_tokens(iter([t]).next)
    result = reduce(tokenizer,0)
    tokenizer.close()
    return result

#tree('+ + + 1 2 3')
