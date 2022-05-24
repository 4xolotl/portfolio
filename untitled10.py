import pyperclip
onum = ['①', '②', '③', '④', '⑤']
txt = ''
n_line = 0
while (True):
    print()
    m = int(input("1: 본문\n2: 종료"))
    if m==1:
        a = input("입력: \n")
        for i in range(30):
            a = a.replace('\n\n', '\n')
        a = a.replace('▶', '기존유형:')
        a = a.replace('■ Subject / Title', '')
        a = a.replace('\n■ Teacher’s Note', '')
        # for i in onum:
        #     a= a.replace(f' ( {i} ) ', ' ')
        
        
        print("====================")
        
        for i in range(0, len(a)):
            if (a[i] >= '⓫' and a[i] <= '⓳') or (a[i] >= '❶' and a[i] <= '❿'):
                txt += '\n'
            if (a[i]== '①'):
                txt += '\n'
            if a[i] == '⑤':
                if (a[i-2] <= 'z' or a[i-2] >= 'A'):
                    n_line += 2
            if n_line > 0 and a[i] == '\n':
                txt += '\n'
                n_line -= 1
            txt += a[i]
        print(txt)
        pyperclip.copy(txt)
    elif m==2:
        break
    else:
        continue