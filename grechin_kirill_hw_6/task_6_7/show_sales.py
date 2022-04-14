import sys

with open('bakery.csv', encoding='utf-8') as bakery:
    if len(sys.argv) == 1 or len(sys.argv) == 2:
        start, stop = 1, sum(1 for line in bakery)
        if len(sys.argv) == 2:
            start = int(sys.argv[1])
        bakery.seek(0)
    elif len(sys.argv) == 3:
        start, stop = int(sys.argv[1]), int(sys.argv[2])
    else:
        print('args error')
        sys.exit(1)
    lines = (line.strip() for index, line in enumerate(bakery, start=1) if start <= index <= stop)
    print(*lines, sep='\n')
