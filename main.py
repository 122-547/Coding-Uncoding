'''        _____       _______       ________       ____     ____   ___        _____
         /  ____|    /  ___   \     |   ___  \     |___|    |    \ |   |     /  ___/
        |  |        |  |   |  |     |  |   \  \    ____     |     \|   |    |  |
        |  |        |  |   |  |     |  |   |  |   |   |     |          |    |  | ___
        |  |___     |  |___|  |     |  |___|  |   |   |     |   |\     |    |  |_\  \
        \______|    \________/      |________/    |___|     |___| \ ___|    \______/
'''
classO = list("\ '><.,/|}{][=+-_)(*&?:^%;$#"+'"@!~`0987654321mnbvcxzlkjhgfdsapoiuytrewqMNBVCXZLKJHGFDSAPOIUYTREWQ')
classN = list('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890`~!@"'+"#$;%^:?&*()_-+=[]{}\|/,.<>' ")
text = txt = ''
num = 0
def coding():
    global txt, text, file_name, final_file_name
    with open(file_name, 'r') as file:
        with open(final_file_name, 'w') as write:
            for i in file:
                a = len(i)
                b = list(i)


                for t in range(0, a):

                    for df in range(0, 95):

                        if b[t] == classN[df]:
                            txt = classO[df]
                        elif b[t] == '\n':
                            txt = '\n'
                        text = '' + txt
                    write.write(text)
def uncoding():
    global text, txt, file_name1, final_file_name1
    with open(file_name1, 'r') as file:
        with open(final_file_name1, 'w') as write:
            for i in file:
                a = len(i)
                b = list(i)

                for t in range(0, a):
                    for df in range(0, 95):
                        if b[t] == classO[df]:
                            txt = classN[df]
                        elif b[t] == '\n':
                            txt = '\n'
                    text = '' + txt
                    write.write(text)
ask = input('Coding:Uncoding:~~ ')
if ask == 'Coding':
    file_name = input('Coding:file_name: ')
    final_file_name = input('Coding:final_file_name: ')
    coding()
elif ask == 'Uncoding':
    file_name1 = input('Uncoding:file_name: ')
    final_file_name1 = input('Uncoding:final_file_name: ')
    uncoding()