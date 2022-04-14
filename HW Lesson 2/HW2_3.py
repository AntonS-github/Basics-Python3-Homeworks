'''3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
Эта задача намного серьёзнее, чем может сначала показаться.'''

array = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index = 0
new_array = []
for i in array:
	if i.lstrip('+-').isdigit():
		index = array.index(i)
		if i.startswith('+'):
			pref='+'
		else: pref = ''
		array.pop(index)
		i = f'"{pref}{0}{int(i)}"'
		array.insert(index,i)
print(array)
print(" ".join(array))