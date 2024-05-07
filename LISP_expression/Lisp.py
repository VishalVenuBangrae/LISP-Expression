import sys, traceback

from LispParser import parser


def read_input():
    result = ''
    while True:
        data = input('LISP: ').strip()
        if ';' in data:
            i = data.index(';')
            result += data[0:i + 1]
            break
        else:
            result += data + ' '
    return result


def evalNum(tree):
    if tree[0] == 'num':
        return tree[1], "OK"
    elif tree[0] == '+':
        result1, message1 = evalNum(tree[1])
        if message1 != "OK":
            return None, message1
        result2, message2 = evalNum(tree[2])
        if message2 != "OK":
            return None, message2
        return result1 + result2, "OK"
    elif tree[0] == '-':
        result1, message1 = evalNum(tree[1])
        if message1 != "OK":
            return None, message1
        result2, message2 = evalNum(tree[2])
        if message2 != "OK":
            return None, message2
        return result1 - result2, "OK"
    elif tree[0] == '*':
        result1, message1 = evalNum(tree[1])
        if message1 != "OK":
            return None, message1
        result2, message2 = evalNum(tree[2])
        if message2 != "OK":
            return None, message2
        return result1 * result2, "OK"
    elif tree[0] == '/':
        result1, message1 = evalNum(tree[1])
        if message1 != "OK":
            return None, message1
        result2, message2 = evalNum(tree[2])
        if message2 != "OK":
            return None, message2
        if result2 == 0:
            return None, "EVALUATION ERROR: Divide by 0!"
        return result1 / result2, "OK"
    elif tree[0] == 'car':
        result1, msg = evalList(tree[1])
        if msg != "OK":
            return None, msg
        if not result1:
            return None, "Cannot evaluate CAR of EMPTY List!"
        return result1[0], "OK"
    else:
        return None, "CDR of empty list Error!"


def evalList(tree):
    if not tree:
        return [], "OK"
    if tree[0] == 'cdr':
        if len(tree) != 2:
            return None, "CDR of empty list Error!"
        res, msg = evalList(tree[1])
        if msg != "OK":
            return None, msg
        if not res:
            return None, "Cannot evaluate CDR of EMPTY List!"
        return res[1:], "OK"
    else:
        res, msg = evalNum(tree[0])
        if msg != "OK":
            return None, msg
        res_list, msg = evalList(tree[1])
        if msg != "OK":
            return None, msg
        return [res] + res_list, "OK"


def main():
    while True:
        data = read_input()
        if data == 'exit;':
            break
        try:
            tree = parser.parse(data)
            print(tree)
            if tree[0] == 'NUM':
                answer, msg = evalNum(tree[1])
                if msg == "OK":
                    print("\nThe value is " + str(answer) + "\n")
                else:
                    print("\n" + msg + "\n")
            elif tree[0] == 'LIST':
                answer, msg = evalList(tree[1])
                if msg == "OK":
                    print("\nThe value is " +
                          str(answer).replace('[', '(').replace(']', ')').replace(',', '') + "\n")
                else:
                    print("\n" + msg + "\n")
            else:
                continue
        except Exception as inst:
            continue


main()
