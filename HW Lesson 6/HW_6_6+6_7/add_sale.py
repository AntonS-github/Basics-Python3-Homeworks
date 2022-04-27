import sys
with open('bakery.csv', 'a+', encoding = 'utf-8') as tab:
	tab.seek(0)
	tab.writelines(sys.argv[1] + '\n')



