
def simplifyPath(path: str) -> str:

    if len(path )==1:
        return "/"
    path_list =path.split('/')
    stack =["/"]
    for i in path_list:
        if i== "":
            pass
        elif i == "..":
            if stack[-1] == '/':
                pass
            else:
                stack.pop()
        elif i == ".":
            pass
        else:
            stack.append(i)

    res = ""
    for j in stack:
        r = "/" + j
        res += r

    if len(res) == 2:
        return res[1:]
    return res[2:]

if __name__ == '__main__':
    print(simplifyPath("/../"))