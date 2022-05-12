import os
import shutil
#Заполнение стартера проекта
level_2_dirs = ['settings', 'mainapp', 'authapp']
for dir in level_2_dirs:
	os.makedirs(os.path.join('my_project', dir), exist_ok=True)
	if dir == 'settings':
		os.chdir('my_project/settings')
		with open('__init__.py', 'x'), open('dev.py', 'x'), open('prod.py', 'x'):
			os.chdir('../..')
	elif dir == 'mainapp':
		os.chdir('my_project/mainapp')
		os.makedirs(os.path.join('templates', 'mainapp'))
		with open('__init__.py', 'x'), open('models.py', 'x'), open('views.py', 'x'):
			os.chdir('../..')
	elif dir == 'authapp':
		os.chdir('my_project/authapp')
		os.makedirs(os.path.join('templates', 'authapp'))
		with open('__init__.py', 'x'), open('models.py', 'x'), open('views.py', 'x'):
			os.chdir('../..')
path_1 = os.path.join('my_project', 'mainapp', 'templates', 'mainapp', 'base.html')
path_2 = os.path.join('my_project', 'mainapp', 'templates', 'mainapp', 'index.html')
path_3 = os.path.join('my_project', 'authapp', 'templates', 'authapp', 'base.html')
path_4 = os.path.join('my_project', 'authapp', 'templates', 'authapp', 'index.html')
with open (path_1, 'x'), open(path_2, 'x'), open(path_3, 'x'), open(path_4, 'x'):
	pass
os.makedirs('my_project/all_templates', exist_ok=True)
new_path = os.path.join('my_project', 'all_templates')
for root, dirs, files in os.walk('my_project'):
	for file in files:
		if file.endswith('html'):
			dir = os.path.basename(root)
			#print(os.path.join(dir, file))
			#print(os.path.join(new_path, dir, file))
			shutil.copytree(root, os.path.join(new_path, dir), dirs_exist_ok=True)

    

