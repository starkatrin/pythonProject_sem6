
def list_complex(inp_str):
    res = []
    n = 0
    for i in range(len(inp_str)):
        if inp_str[n].isdigit():
            if n+1 < len(inp_str) and inp_str[n+1] == '.':
                res.append(float(inp_str[n]+inp_str[n+1]+inp_str[n+2]))
                n = n + 2
            else:
                res.append(float(inp_str[n]))
        i = n
        if inp_str[i] == '(':
            while inp_str[i] != ')':
                i += 1
            res.append(complex(inp_str[n:i+1]))
        n = i + 1
        if n >= len(inp_str):
            return res
        if inp_str[n] in ('-','+', '*','/', '^'):
            res.append(inp_str[n])

    return res

def calculator(calc_list):
    if len(calc_list) == 1:
        return calc_list[0]
    for sign in ('^', '*','/','-','+'):
        for i in range(len(calc_list)):
            if calc_list[i] == sign:
                left, op, right = calc_list[i-1], calc_list[i], calc_list[i+1]
                if op == '^':
                    ans = (left) ** (right)
                    calc_list[i] = ans
                    calc_list.remove(left)
                    calc_list.remove(right)
                    return calculator(calc_list)
                elif op == '*':
                    ans = (left) * (right)
                    calc_list[i] = ans
                    calc_list.remove(left)
                    calc_list.remove(right)
                    return calculator(calc_list)
                elif op == '/':
                    ans = (left) / (right)
                    calc_list[i] = ans
                    calc_list.remove(left)
                    calc_list.remove(right)
                    return calculator(calc_list)
                elif op == '+':
                    ans = (left) + (right)
                    calc_list[i] = ans
                    calc_list.remove(left)
                    calc_list.remove(right)
                    return calculator(calc_list)
                elif op == '-':
                    ans = (left) - (right)
                    calc_list[i] = ans
                    calc_list.remove(left)
                    calc_list.remove(right)
                    return calculator(calc_list)

inp_str = '(2.3+5j)+3*(5+7j)-6*5.1'
calc_list = list_complex(inp_str)
answer = calculator(calc_list)
print(answer)


# #
# #
# print(calculation('1+2*(3+3)'))
# #def calc_complex:
