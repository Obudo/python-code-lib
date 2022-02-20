def process_array(input_array, extra_args, on_pop, on_append, condition):
    retval = []
    for element in input_array:
        while retval and condition(element, retval, extra_args):
            on_pop(retval, extra_args)
            retval.pop()
        retval.append(element)
        on_append(retval, extra_args)
        
    return retval


def removeKdigits(num, k):
    extra_args = {'k': k, 'removed':  0}
    def on_pop(_, extra):
        extra['removed'] += 1
    on_append = lambda *_ : None
    condition = lambda el, stack, extra : el < stack[-1] and extra['removed'] < extra['k']

    result_stack = process_array(num, extra_args, on_pop, on_append, condition)
    
    if extra_args['removed'] < k:
        result_stack = result_stack[:extra_args['removed'] - k]
        
    return str(int("".join(result_stack or ['0'])))

if __name__ == '__main__':
    num = []
    k = 5
    print(removeKdigits(num, k))