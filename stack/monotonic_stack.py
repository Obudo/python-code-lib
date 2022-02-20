def build_monotonic_stack(input_array, extra_args, on_pop, on_append, condition):
    '''
    Builds a monotonick stack using input array.
    Decides whether a candidate can join the stack or if it needs to remove elements
    by calling condition on the element and stack.
    Calls on_pop before removing element and on_append after appending element.
    extra args is a dict passed to every function for flexibility.
    '''
    retval = []
    for element in input_array:
        while retval and condition(element, retval, extra_args):
            on_pop(retval, extra_args)
            retval.pop()
        retval.append(element)
        on_append(retval, extra_args)
        
    return retval

'''
Example problem:
https://leetcode.com/problems/remove-k-digits/
'''

def removeKdigits(num, k):
    extra_args = {'k': k, 'removed':  0}
    def on_pop(_, extra):
        extra['removed'] += 1
    on_append = lambda *_ : None
    condition = lambda el, stack, extra : el < stack[-1] and extra['removed'] < extra['k']

    result_stack = build_monotonic_stack(num, extra_args, on_pop, on_append, condition)
    
    if extra_args['removed'] < k:
        result_stack = result_stack[:extra_args['removed'] - k]
        
    return str(int("".join(result_stack or ['0'])))

if __name__ == '__main__':
    num = "30268139327235013615834656035097148745856468378430"
    k = 20
    print(removeKdigits(num, k))