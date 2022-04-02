import sys

with open('bakery.csv', encoding='utf-8') as bakery:
    if len(sys.argv) == 1 or len(sys.argv) == 2:
        bakery.seek(0)
        if len(sys.argv) == 2:
            bakery.seek((int(sys.argv[1]) - 1) * 8)
        for line in bakery:
            print(line.strip())
    elif len(sys.argv) == 3:
        bakery.seek((int(sys.argv[1]) - 1) * 8)
        lines_count = int(sys.argv[2]) - int(sys.argv[1]) + 1
        for _ in range(lines_count):
            print(bakery.readline().strip())
    else:
        print('args error')
