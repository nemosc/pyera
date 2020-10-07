from util.singleton_meta import SingletonMeta


class IO(metaclass=SingletonMeta):
    def __init__(self):
        pass

    def get_string(self):
        while True:
            try:
                s = input('提示：输入string')
                break
            except:
                pass
        return s

    def get_int(self):
        while True:
            try:
                s = input('提示：输入int')
                i = int(s)
                break
            except:
                pass
        return i


    def get_list(self):
        while True:
            try:
                s = input('提示：输入list')
                l = list(s)
                break
            except:
                pass
        return l

    def put_string(self, s):
        print(s)

    def put_list(self, l):
        for i in range(len(l)):
            print(f'[{i}] {l[i]}')
