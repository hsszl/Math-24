import random
import re

inp = input("Enter 4 numbers separated by space: ").split(" ")
if inp == [""]:
    nums = [random.randint(1, 13) for x in range(4)]
    print(nums, end="")
    input()
else:
    nums = [int(x) for x in inp]

operators = ["+", "-", "*", "/"]
num1 = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 10, "J": 11, "Q": 12, "K": 13}
num2 = {1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "0", 11: "J", 12: "Q", 13: "K"}
outs = []

for ia in range(4):
    for ib in range(4):
        if ia == ib:
            continue
        for ic in range(4):
            if ia == ic or ib == ic:
                continue
            for id in range(4):
                if ia == id or ib == id or ic == id:
                    continue
                a = nums[ia]
                b = nums[ib]
                c = nums[ic]
                d = nums[id]
                for op1 in operators:
                    for op2 in operators:
                        for op3 in operators:
                            if eval(f"(({a} {op1} {b}) {op2} {c}) {op3} {d}") == 24:
                                outs.append(f"{num2[a]}{num2[b]}{num2[c]}{num2[d]}0{op1}{op2}{op3}")
                            if ((op2 == "*" or op2 == "/") and (op3 == "+" or op3 == "-") and
                                    eval(f"({a} {op1} {b}) {op2} ({c} {op3} {d})") == 24):
                                outs.append(f"{num2[a]}{num2[b]}{num2[c]}{num2[d]}1{op1}{op2}{op3}")

solves = []
for solve in outs:
    op1 = solve[-3]
    op2 = solve[-2]
    op3 = solve[-1]
    n1 = num1[solve[0]]
    n2 = num1[solve[1]]
    n3 = num1[solve[2]]
    n4 = num1[solve[3]]
    if solve[-4] == "0":
        if op2 == "+" or op2 == "-":
            if op3 == "+" or op3 == "-":
                solves.append(f"{n1} {op1} {n2} {op2} {n3} {op3} {n4}")
            else:
                solves.append(f"({n1} {op1} {n2} {op2} {n3}) {op3} {n4}")
        else:
            if op3 == "+" or op3 == "-":
                solves.append(f"({n1} {op1} {n2}) {op2} {n3} {op3} {n4}")
            else:
                solves.append(f"(({n1} {op1} {n2}) {op2} {n3}) {op3} {n4}")
    elif solve[-4] == "1":
        solves.append(f"({n1} {op1} {n2}) {op2} ({n3} {op3} {n4})")

for s in solves:
    print(s + " = 24")

solve = 0
for abc in range(len(outs)):
    i_s = 0
    for abd in range(len(solves)):
        s = solves[i_s]
        times = 0
        if solve > len(outs) - 1:
            break
        if s != solves[solve]:
            ajfisdf = solves[solve]
            now = outs[solve]
            for ops in range(3):
                op = now[-3 + ops]
                n = num1[now[ops + 1]]
                if (re.search((op if op in ["-", "/"] else f"[{op}]") + " " + str(n), s) or
                        (op == "+" and (re.match(f"{n} ", s) or re.match(f"[(]{n} ", s)))
                        or (op == "*" and (re.search(f"{n} [*] ", s)) or (re.search(f" [*] {n}", s)))):
                    times += 1
        else:
            i_s += 1
            continue
        if times == 3:
            print(solves[solve] + " = " + s)
            del solves[i_s]
            del outs[i_s]
            i_s -= 1
        else:
            print(solves[solve] + " != " + s)
        i_s += 1
    solve += 1

print("\n化简后：")
for s in solves:
    print(s + " = 24")
