import sys

if len(sys.argv) == 4:
    print(int(sys.argv[1]) * int(sys.argv[2]) + int(sys.argv[3]))
else:
    print('Нужно больше данных.')
