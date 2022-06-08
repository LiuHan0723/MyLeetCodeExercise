
def evalRPN(tokens) -> int:
    stack =[]
    for i in tokens:
        if i== "+":
            v1 = int(stack.pop())
            v2 = int(stack.pop())
            pushV = v1 + v2
            stack.append(pushV)
        elif i == "-":
            v1 = int(stack.pop())
            v2 = int(stack.pop())
            pushV = v2-v1 ###注意注意！
            stack.append(pushV)
        elif i == "*":
            v1 = int(stack.pop())
            v2 = int(stack.pop())
            pushV = v1 * v2
            stack.append(pushV)
        elif i == "/":
            v1 = int(stack.pop())
            v2 = int(stack.pop())
            pushV = int(v2/v1) ###注意注意！###注意注意！###注意注意！###注意注意！
            stack.append(pushV)
        else:
            stack.append(i)
    return int(stack.pop())

def isValid(s):
    if len(s) <= 1:
        return False

    stack = []
    for i in s:
        match = None
        if i == ")":
            match = "("
        elif i == "}":
            match = "{"

        elif i == "]":
            match = "{"
        else:
            stack.append(i)
            continue

        if match and stack:
            if match != stack.pop():
                return False
        else:
            return False

    if stack:
        return False

    else:

        return True
if __name__ == '__main__':
    # print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    print(isValid(")(){}"))