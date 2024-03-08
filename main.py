import pyperclip

a = """
Your file content goes here!
HTML, CSS, JS
"""

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def replace_links(option):
    if option == 1:
        found = []
        for i in list(find_all(a, 'https://media')):
            found.append(i)
        length = 80
        to_replace = []
        for key in found:
            c = key+length
            to_replace.append(a[key:c])
        return to_replace
    elif option == 2:
        found = []
        for i in list(find_all(a, 'https://cdn')):
            found.append(i)
        length = 78
        to_replace = []
        for key in found:
            c = key+length
            to_replace.append(a[key:c])
        return to_replace

for i in range(2):
    _ = i+1
    x = replace_links(_)
    for j in x:
        print(j)
        a = a.replace(j, "/images/main")
        
pyperclip.copy(a)
