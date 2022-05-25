import pyperclip
onum = ['①', '②', '③', '④', '⑤']
txt = ''
a = ''
n_line = 0
while (True):
    print()
    m = int(input("1: 본문\n2: 종료"))
    if m==1:
        f = open('./test.txt', 'r', encoding='utf-8-sig')
        lines = f.readlines()
        for i in lines:
            a += i
        for i in range(30):
            a = a.replace('\n\n', '\n')
        a = a.replace('▶', '================================================\n기존유형:')
        a = a.replace('■ Subject / Title', '')
        a = a.replace('\n■ Teacher’s Note', '')
        
        
        print("====================")
        
        for i in range(0, len(a)):
            if a[i] == '❶':
                txt += '\n'
            if (a[i] >= '⓫' and a[i] <= '⓳') or (a[i] >= '❶' and a[i] <= '❿'):
                if (a[i-4] >= 'A' and a[i-4] <='z'):
                    txt += '\n'
            if (a[i]== '①' and a[i-2] != '('):
                if not (a[i] >= '⓫' and a[i] <= '⓳') or (a[i] >= '❶' and a[i] <= '❿'):
                    txt += '\n'
            if a[i] == '⑤':
                if (a[i-2] <= 'z' or a[i-2] >= 'A'):
                    n_line += 2
            if n_line > 0 and a[i] == '\n':
                txt += '\n'
                n_line -= 1
            txt += a[i]
        for i in range(5):
            txt = txt.replace('\n\n\n', '\n\n')
            txt = txt.replace('  ', ' ')
        out = open('out.txt', 'w', encoding='utf-8-sig')
        out.write(txt)
        out.close()
        f.close()
        pyperclip.copy(txt)
    elif m==2:
        break
    else:
        print()