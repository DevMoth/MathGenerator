import random
from calculator import calc_expr
def join_expression(opers, nums):
    expr = nums[0]
    for i in range(len(opers)):
        expr = expr + opers[i] + nums[i+1]
    return expr
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
