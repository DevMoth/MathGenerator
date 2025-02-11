from calculator import calc_expr
from generator import *
import random
def gen_expr_tuned():
    return generate_braces_expression(random.randint(1, 4), [1,10], ["+","-"],
                                    brace_count = random.randint(1, 2), max_brace_depth = 1, max_brace_opers = 2,
                                    allow_negative = False)
class Config:
    oper_count_range = [1, 3]
    num_range = [1, 10]
    allowed_opers = ["+", "-"]
    brace_count_range = [1,2]
    max_brace_depth = 1
    max_brace_opers = 2
    allow_negative = False
def gen_expr_from_config(conf):
    return generate_braces_expression(random.randint(conf.oper_count_range[0], conf.oper_count_range[1]), conf.num_range, conf.allowed_opers,
                                    brace_count = random.randint(conf.brace_count_range[0], conf.brace_count_range[1]), max_brace_depth = conf.max_brace_depth, max_brace_opers = conf.max_brace_opers,
                                    allow_negative = conf.allow_negative)
config = Config()
rounds = int(input("INPUT ROUNDS COUNT: "))
errors = [0 for i in range(rounds)]
for i in range(rounds):
    print(i+1,"/",rounds, sep = "", end = " ")
    print("Реши это выражение:")
    expr = gen_expr_from_config(config)
    print(expr+"=?")
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
print("Молодец, ты все решил, вот твои результаты:")
for i in range(max(errors)):
    print("".join([["  ", "0 "][a >= max(errors)-i] for a in errors]))
print("".join([str(i+1)+" " if i < 10 else str(i+1) for i in range(rounds)]))
print("Всего ошибок:",sum(errors))
