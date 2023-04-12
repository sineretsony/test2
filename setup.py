import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

setup(name='ELLE',
      version='1.0',
      description='Covert files ADS and AI in PDF',
      options={'build_exe': {'packages': [], 'include_files': ['UFO2.ico']}},
      executables=[Executable('ELLE.py', base=base, icon='UFO2.ico')],
      target='cx_Freeze')

#python setup.py build