from calculator import calc_expr
from generator import *
import random

# Legacy expression generator function
def gen_expr_tuned():
    return generate_braces_expression(random.randint(1, 4), [1,10], ["+","-"],
                                    brace_count = random.randint(1, 2), max_brace_depth = 1, max_brace_opers = 2,
                                    allow_negative = False)
# Class for storing configuration information about expression parameters
class Config:
    Params = dict(
        oper_count_range = [1, 3],
        num_range = [1, 10],
        allowed_opers = ["+", "-"],
        brace_count_range = [1,2],
        max_brace_depth = 1,
        max_brace_opers = 2,
        allow_negative = False,
        )
    # () operator for returning the dictionary with parameters
    def __call__(self):
        return self.Params
    # prints all available parameters to the console
    def show(self):
        for key in self.Params.keys():
            print(key, self.Params[key])
    # converts a given output to a string for saving
    def sanitize_output(self, output):
        if isinstance(output, int):
            return str(output)
        if isinstance(output, bool):
            return str(output)
        if isinstance(output, str):
            return output
        if isinstance(output, list):
            s = ""
            for a in output:
                s += self.sanitize_output(a)+" "
            return s[:-1]
    # saves the configuration to a text file
    def save(self, filename = "config.txt"):
        f = open(filename, "w")
        for key in self.Params.keys():
            f.write(f"{key}: {self.sanitize_output(self.Params[key])}\n")

    # convert input string or a list of input strings to workable data types
    def sanitize_input(self, inp):
        if isinstance(inp, str):
            if all([a in "1234567890.-" for a in inp]) and inp != "-":
                if "." in inp:
                    return float(inp)
                return int(inp)
            if inp == "False":
                return False
            if inp == "True":
                return True
            return inp
        if isinstance(inp, list):
            if len(inp) == 1:
                return self.sanitize_input(inp[0])
            return [self.sanitize_input(a) for a in inp]
    # load the configuration from a text file
    def load(self, filename = "config.txt"):
        f = open(filename, "r")
        for line in f.readlines():
            line = line.split()
            key = line[0][:-1]
            param = line[1:]
            self.Params[key] = self.sanitize_input(param)
    # Initialize a config object by loading a given text file
    def __init__(self, filename):
        self.load(filename)

# Generates an expression with parameters from a given config
def gen_expr_from_config(conf):
    return generate_braces_expression(
            random.randint(conf()["oper_count_range"][0], conf()["oper_count_range"][1]),
            conf()["num_range"],
            conf()["allowed_opers"],
            brace_count = random.randint(conf()["brace_count_range"][0], conf()["brace_count_range"][1]),
            max_brace_depth = conf()["max_brace_depth"],
            max_brace_opers = conf()["max_brace_opers"],
            allow_negative = conf()["allow_negative"]
            )

# Main program
config = Config("config.txt")
rounds = int(input("INPUT ROUNDS COUNT: "))
errors = [0 for i in range(rounds)]
# Round loop
for i in range(rounds):
    print(i+1,"/",rounds, sep = "", end = " ")
    print("Реши это выражение:")
    expr = gen_expr_from_config(config)
    print(expr+"=?")
    # Answering loop (user has to type the correct answer or SKIP to get to the next round
    while 1:
        try:
            answer = input()
            if answer == "SKIP" or float(answer) == calc_expr(expr):
                print("Правильно!")
                break
            else:
                print("Неправильно...")
                errors[i] += 1
        except:
            print("Неправильно...")
            errors[i] += 1
# Error statistic (error count per round + total error count)
print("Молодец, ты все решил, количесвто ошибок по вопросам:")
for i in range(max(errors)):
    print("".join([["  ", "0 "][a >= max(errors)-i] for a in errors]))
print("".join([str(i+1)+" " if i < 10 else str(i+1) for i in range(rounds)]))
print("Всего ошибок:",sum(errors))
