
def main(args):
	codes = dict()
	symbols,number = map(int, input().split())
	for a in range(symbols):
		e,d = map(str, input().split())
		e = e[:-1]
		codes[d] = e 
	findstr = str(input())
	i = 1
	x = 0
	itog = ""
	while(len(findstr)!=x):
		strochka = findstr[x:i]
		for key in codes:
			if(key == strochka):
				itog = itog + codes[key]
				x = i
		i=i+1
	print(itog)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
