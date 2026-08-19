import random
from calculator import calc_expr

# given an expression in the form of a list of operators and a list of numbers, returns the expression in the form of a string
def join_expression(opers, nums):
    expr = nums[0]
    for i in range(len(opers)):
        expr = expr + opers[i] + nums[i+1]
    return expr
# Given operation count, allowed range of numbers, allowed operators, list of already generated expressions to be counted as numbers and a flag to allow negative answers
# Returns an expression of the form: ex_1 oper_1 ex_2 oper_2 ... ex_n, where ex_i is either a known expression from known_nums or a new generated number and oper_i is a certain operator
def generate_simple_expression(oper_count, num_range, allowed_opers = ["+", "-", "*", "/"],
                               known_nums = [],
                               allow_negative = True):
    opers = [random.choice(allowed_opers) for i in range(oper_count)]
    nums = known_nums + [str(random.randint(num_range[0], num_range[1])) for i in range(0, oper_count+1-len(known_nums))]
    random.shuffle(nums)
    expr = join_expression(opers, nums)
    if calc_expr(expr) >= 0 or allow_negative:
        return expr
    return generate_simple_expression(oper_count, num_range, allowed_opers, known_nums, allow_negative)
# Given a list of parameters, returns complex expression with brackets ( example: (1 + 2 + 3) - 4 + 5 - (7 - 6) )
def generate_braces_expression(oper_count, num_range, allowed_opers = ["+", "-", "*", "/"],
                               brace_count = 2, max_brace_depth = 2, max_brace_opers = 2,
                               allow_negative = True):
    braces = []
    if max_brace_depth > 0:
        for i in range(brace_count):
            oper_count = random.randint(1, max_brace_opers)
            inner_brace_count = random.randint(1, brace_count)
            braces.append("("+generate_braces_expression(oper_count, num_range, allowed_opers, inner_brace_count, max_brace_depth-1, max_brace_opers, allow_negative)+")")
    expr = generate_simple_expression(oper_count, num_range, allowed_opers, braces, allow_negative)
    if calc_expr(expr) >= 0 or allow_negative:
        return expr
    return generate_braces_expression(oper_count, num_range, allowed_opers, brace_count, max_brace_depth, max_brace_opers, allow_negative)
