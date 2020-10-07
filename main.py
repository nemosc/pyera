from util.io import IO
from game.save import Save
import os
import re
import pickle
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

SAVE_NUM = 20

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    io = IO()
    io.put_string('duel!')
    io.put_list(['保存', '读取', '开始'])
    i = io.get_int()
    if i==0:
        try:
            save = ['-'*20]*SAVE_NUM
            for file in os.listdir('save'):
                m = re.match(r'save[0-9]{2}.sav',file)
                if m is not None and int(m)<len(save):
                    p = pickle.load(os.path.join())
                    save[int(m)] = p.get_digest()
                    del p
        except:
            pass
        io.put_list(save)
    elif i==1:
        try:
            save = ['-'*20]*SAVE_NUM
            for file in os.listdir('save'):
                m = re.match(r'save[0-9]{2}.sav',file)
                if m is not None and int(m)<len(save):
                    p = pickle.load(os.path.join())
                    save[int(m)] = p.get_digest()
                    del p
        except:
            pass
        io.put_list(save)
    elif i==2:
        pass
    l = io.get_list()
    print(f'get_list = {str(l)}')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
