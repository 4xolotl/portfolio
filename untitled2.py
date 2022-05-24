import pyperclip

txt = ''

while (True):
    print()
    m = int(input("1: 본문\n2: 어휘\n3: 종료\n"))
    if m==1:
        a = input("입력: \n")
        print("====================")
        
        for i in range(0, len(a)):
            if (a[i] >= '⓫' and a[i] <= '⓳') or (a[i] > '❶' and a[i] <= '❿'):
                txt += '\n'
            txt += a[i]
        print(txt)
        pyperclip.copy(txt)
        
    elif m==2:
        a = input("입력: \n")
        
        print("====================")
        
        for i in a:
            if i != "\n":
                if i == '	':
                    print(' ', end='')
                else:
                    print(i, end='')
    elif m==3:
        break
    