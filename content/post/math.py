# Change LaTex to MathJax
# specifically, solve the problem of subscript

import os
import re
import codecs
import shutil

# https://stackoverflow.com/questions/31005138/replace-regex-matches-in-a-string-with-items-from-a-list-in-order


remove1 = lambda p : p.replace('[^\$]', '').replace('\\', '')
remove2 = lambda p : p.replace('\\', '')
add_math = lambda s, p1, p2, f : f(p1) + s + f(p2)

def replace(txt, p, f):
    math = re.findall(p, txt)
    results = []
    for m in math:
        if type(m) is tuple:
            m = m[0]
        if '_' not in m:
            results.append(m)
            continue
        i = 0
        while (i < len(m)):
            if m[i] == '_' and i > 0 and m[i-1] != '\\':     
                m = m[:i] + '\\' + m[i:]
                i += 1
            i += 1
        results.append(m)
    i1, i2 = p.find('('), len(p) - p[::-1].find(')') - 1
    p1, p2 = p[:i1], p[i2 + 1:]
    results = [add_math(s, p1, p2, f) for s in results]
    txt = re.sub(p, lambda x: results.pop(0), txt)
    return txt

ROOT = r'D:\Hugo\blog\content\post'
REDIRECT = r'D:\Hugo\blog\archive\_post'
CHECKLIST = r'D:\Hugo\blog\content\post\checklist.txt'

with codecs.open(CHECKLIST, 'r', 'utf-8') as f:
    checklist = f.read().split('\n')
    
for p in os.listdir(ROOT):
    if '.' in p or p in checklist:
        continue
    input('Confirm to modify ' + p + '?')

    path = os.path.join(ROOT, p, 'index.md')
    if not os.path.exists(path):
        print('no index.md in ' + dir)
        continue
    with codecs.open(path, 'r', 'utf-8') as f:
        text = f.read()
    text = replace(text, '\$\$((.|\n)+?)\$\$', remove2)
    text = replace(text, '\$(.+?)\$', remove1)
    
    shutil.copyfile(path, os.path.join(REDIRECT, p + '.md'))

    with codecs.open(path, 'w', 'utf-8') as f:
        f.write(text)
    with codecs.open(CHECKLIST, 'a', 'utf-8') as f:
        f.write(p + '\n')

    