import sys
from cx_Freeze import setup, Executable

base = None

# # отключаем окно терминала
# if sys.platform == 'win32':
#     base = 'Win32GUI'

setup(name='BARCODEKS.py',
      version='1.0',
      description='',
      options={'build_exe': {'packages': ['os', 'pathlib', 'reportlab', 'sys'], 'include_files': ['Iconka-Cat-Halloween-Cat-ghost.ico']}},
      executables=[Executable('BARCODEKS.py', base=base, icon='Iconka-Cat-Halloween-Cat-ghost.ico')])


#python setup.py build