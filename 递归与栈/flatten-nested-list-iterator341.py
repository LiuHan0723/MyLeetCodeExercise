
###栈实现
class Flatten:

    def __init__(self,lists):
        self.stack=[]
        for i in range(len(lists)-1,-1,-1):
            self.stack.append(lists[i])

    def next(self):
        return self.stack.pop()
    def hasNext(self):
        while self.stack:
            top=self.stack[-1]
            if isinstance(top,int):
                return True
            else:
                self.stack.pop()
                for i in range(len(top)-1,-1,-1):
                    self.stack.append(top[i])


        return False




if __name__ == '__main__':
    test=[[1,2,[3,4],4,[[5,6,[6]]]]]

    fla=Flatten(test)

    print(fla.hasNext())
    print(fla.next())
    print(fla.hasNext())
    print(fla.next())