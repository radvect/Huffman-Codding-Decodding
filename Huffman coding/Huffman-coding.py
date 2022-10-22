import copy
def sorting(symb_freq):
	symb_freq.sort(key = lambda x: x[1])
	return(symb_freq)
"""def filling(symbfreq, i):
	for elem in range(0,i,1):
		symbfreq[elem][2] = "0"+symbfreq[elem][2]
	return symbfreq
	"""
	
def main(args):
	strochka = str(input())
	strochka1 = strochka
	strochkasaved = strochka
	symb_freq = []
	
	
		
	for symb in strochka:
		iteratorforcycle = 0
		for i in range(len(symb_freq)):
			if(symb_freq[i][0] == symb):
				symb_freq[i][1] = symb_freq[i][1] + 1
			else:
				iteratorforcycle = iteratorforcycle+ 1
		if(iteratorforcycle == len(symb_freq)):
			symb_freq.append([symb,1,""])
			strochka = strochka[1:]
	symb_freq=list(sorting(symb_freq))
	symb_freq1 =  copy.deepcopy(symb_freq)
	finalfreq = copy.deepcopy(symb_freq)
	
	while(len(symb_freq1)!=1):
		symb_freq1.append([symb_freq1[0][0]+symb_freq1[1][0],symb_freq1[0][1]+symb_freq1[1][1],""])
		symb_freq.append([symb_freq1[0][0]+symb_freq1[1][0],symb_freq1[0][1]+symb_freq1[1][1],""])
		symb_freq1.pop(0)
		symb_freq1.pop(0)
		sorting(symb_freq1)
		sorting(symb_freq)
	#print(symb_freq1)
	"""for a in range(0,len(finalfreq),1):
		if(a % 2 == 1):
			finalfreq[a][2] = "1"
		else:
			#finalfreq[a][2]="0" 
			"""
	symb_freq.pop(len(symb_freq)-1)
	#print(finalfreq)
	for a in range(0,len(symb_freq),1):
		if(a % 2 == 1):
			symb_freq[a][2] = "1"
		else:
			symb_freq[a][2]="0"
	#print(symb_freq)
	#print(symb_freq)
	for elt in range(0,len(finalfreq),1):
		finalfreq[elt][2]=""
		
	#print(finalfreq)
	#print(symb_freq)
	
	
	for a in range(0,len(finalfreq),1):
		for b in range(0,len(symb_freq),1):
			for e in range(0,len(symb_freq[b][0]),1):
				s =symb_freq[b][0]
				#print(finalfreq[a][0])
				
				#print(finalfreq[a][0],s[e],symb_freq[b][2], sep = "::")
				
				if(finalfreq[a][0] == s[e]):
					finalfreq[a][2]=symb_freq[b][2]+finalfreq[a][2]
					
					
	#print(finalfreq)
	
	
	
	
	
	
	
	
	"""if(len(symb_freq) == 1):
		symb_freq[0][2] = "0" 
	while(len(symb_freq1)!=1):
		symb_freq[0][2]="0"+symb_freq[0][2]
		symb_freq[1][2]="1"+symb_freq[1][2]
		#filling(symb_freq,c)
		summary = symb_freq1[0][1]+symb_freq1[1][1]
		symb_freq1.append([symb_freq[0][2]+symb_freq[1][2],summary,""])
		symb_freq.append([symb_freq[0][2]+symb_freq[1][2],summary,""])
		symb_freq1.pop(0)
		symb_freq1.pop(0)
		sorting(symb_freq1)
	#symb_freq[0][2] +=1
	x = 0
	z = 1"""
	itog = ""
	#print(symb_freq)
	#print(strochka1)
	#print(itog,1)
	while(len(strochka1)!=0):
		strochka2 = strochka1[0:1]
		#print(strochka2)
		for lsa in range(0,len(finalfreq),1):
			#print(itog)
			if(finalfreq[lsa][0]==strochka2):
				#print(symb_freq[lsa][2])
				#print(finalfreq[lsa][2])
				#print(itog)
				itog =   itog + finalfreq[lsa][2]
				
				#print(symb_freq[lsa][2])
		strochka1 = strochka1[1:]
		
	
	finalfreq.sort(key = lambda x: x[0])
	
	#itog = itog[::-1] 
	laster = ""
	if(len(finalfreq)==1):
		itog = strochkasaved
	print(len(finalfreq), len(itog))
	if(len(finalfreq)==1):
		print(finalfreq[0][0],0,sep =": ")
		for a in range(0,len(strochka)+1,1):
			laster = laster + "0"
		print(laster)
	else:
		for i in range(0,len(finalfreq),1):
			print(finalfreq[i][0],finalfreq[i][2],sep =": ")
		print(itog)
		
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
