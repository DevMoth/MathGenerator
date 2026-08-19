# Given an expression in the form of a string, return the same expression in the form of 2 lists: numbers and operators (expressions in brackets are treated like numbers)
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
# Given 2 numbers and an operator performs the given operation
def calc_oper(num1, num2, oper):
    if oper == "*":
        return num1*num2
    if oper == "/":
        return num1/num2
    if oper == "+":
        return num1+num2
    if oper == "-":
        return num1-num2
# Given a string containing either a number or an expression inside brackets, returns the numerical value of the number or the expression inside brackets
def convert_to_num(string):
    if string[0] == "(":
        return calc_expr(string[1:-1])
    else:
        return float(string)
# Given a list of numbers, list of operators and a string, containing all selected operators, calculates all of the operations, involving the selected operators and returns the modified lists of numbers and remaining operators
def iterate_with_opers(nums, opers, iter_opers):
    i = 0
    while i < len(opers):
        if opers[i] in iter_opers:
            nums[i] = calc_oper(nums[i], nums[i+1], opers[i])
            nums.pop(i+1)
            opers.pop(i)
            i -= 1
        i += 1
# Calculate the answer to a given expression in the form of a string
def calc_expr(string):
    nums, opers = split_expr(string)
    nums = [convert_to_num(x) for x in nums]
    iterate_with_opers(nums, opers, "*/")
    iterate_with_opers(nums, opers, "+-")
    return nums[0]
