def split_expr(string):
    num_ind = 0
    nums = []
    opers = []
    for i in range(len(string)):
        if string[i] in "*/-+":
            bracket_count = string[:i].count("(")-string[:i].count(")")
            if bracket_count == 0:
                opers.append(string[i])
                nums.append(string[num_ind:i])
                num_ind = i+1
    nums.append(string[num_ind:])
    for i in range(len(nums)):
        if nums[i] == "":
            nums[i] = "0"
    return [nums, opers]
def calc_oper(num1, num2, oper):
    if oper == "*":
        return num1*num2
    if oper == "/":
        return num1/num2
    if oper == "+":
        return num1+num2
    if oper == "-":
        return num1-num2
def convert_to_num(string):
    if string[0] == "(":
        return calc_expr(string[1:-1])
    else:
        return float(string)
def iterate_with_opers(nums, opers, iter_opers):
    i = 0
    while i < len(opers):
        if opers[i] in iter_opers:
            nums[i] = calc_oper(nums[i], nums[i+1], opers[i])
            nums.pop(i+1)
            opers.pop(i)
            i -= 1
        i += 1
def calc_expr(string):
    nums, opers = split_expr(string)
    nums = [convert_to_num(x) for x in nums]
    iterate_with_opers(nums, opers, "*/")
    iterate_with_opers(nums, opers, "+-")
    return nums[0]
