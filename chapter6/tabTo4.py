import sys

source = sys.argv[1]
target = sys.argv[2]

file = open(source, encoding="utf-8")
tab_content = file.read()
file.close()

space4_content = tab_content.replace("\t", " "*4)

file = open(target, 'w', encoding="utf-8")
file.write(space4_content)
file.close()
