import tokenize 

#
# DESIGN NOTES:
#
# 1)-I chose not to use classes because there is little state to be stored in a would
#    be object. Having it as a library suffices. Of course the depth could be seen
#    as a state for an object, but the stack does an good job of storing it.
#
# 2)-I assumed a string representation for the trees. The only valid tokens are
#    NUMBERS and OPERATORS as specified in the program. However these language
#    elements are insufficient to express trees that are taller on the left branch.
#    For example:
#         +
#       /   \
#     +      1
#   /  \
# 1     2
#
#    could not be expressed in my grammar. A dfs traversal of the labels would give us
#    + + 1 2 1
#    This would be interpreted as:
#         +
#       /
#     + 
#   /  \  \
# 1     2   1
#    This does not belong to the grammar given that the root is node of arity 1.
#    To address this we would have had to add parenthesis or some other symbol
#    for associating.
#
# 3)-I do not have a 'debug mode' in the code. To achieve this we need to uncomment
#    the print statements in the code.
#

#
# Set of valid operators
#
operators = ['+', '-', '*', '/']

#
# operate - apply binary operator to val1 and val2
#
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


#
# reduce - Given a generator that represents a tree reduce via the
#          mathematical operations
#
#   Chose tu use the tokenizer library to avoid writing a lexer.
#
def reduce(tokenizer, depth):

    childcount = 0
    toktyp,tokval, _,_,_ = tokenizer.next()

    if toktyp == tokenize.OP and any(s in tokval for s in operators):

        #print 'OP ' + tokval + ' ' +str(depth)
        accum = reduce(tokenizer, depth+1)  
        childcount += 1
        #print 'accum1 ' + str(accum) + ' depth ' + str(depth) + ' childcount ' + str(childcount)

        #
        # Enforce node arity is >= 2
        #
        try:
            accum = operate(tokval, accum, reduce(tokenizer, depth+1))
            childcount += 1
            #print 'accum1.5 ' + str(accum) + ' depth ' + str(depth) + ' childcount ' + str(childcount)
        except StopIteration:
            #print 'StopIteration depth ' + str(depth)
            if childcount > 1:
                return accum
            else:
                #print 'Node must be >= 2'
                raise StopIteration

        #print 'accum2 ' + str(accum) + ' depth ' + str(depth) + ' childcount ' + str(childcount)
 
        #
        # Manage the case for > 2
        #
        while True:
            try:
                #print 'accum3 ' + str(accum) + ' depth ' + str(depth) + ' childcount ' + str(childcount)
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
        #print "Habemus NUMBER " + tokval + ' depth ' + str(depth)
        return int(tokval)
    elif toktyp == tokenize.ENDMARKER:
        #print "Habemus ENDMARKER " + ' depth ' + str(depth)
        raise EOFError
    else:
        print "Habemus splat"
        raise SyntaxError

def tree (t):
    tokenizer = tokenize.generate_tokens(iter([t]).next)
    result = reduce(tokenizer,0)
    tokenizer.close()
    return result

