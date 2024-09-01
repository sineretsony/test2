import sys
from cx_Freeze import setup, Executable

base = None

# if sys.platform == 'win32':
#     base = 'Win32GUI'  # Убирает окно консоли, если это нужно

setup(
    name='Tasker',
    version='1.0',
    description='Tasker',
    options={
        'build_exe': {
            'packages': ['asyncio', 'anyio', 'telegram'],
            'includes': ['anyio._backends._asyncio'],
            'include_files': ['Bokehlicia-Captiva-Office-calendar.ico'],
            'excludes': ['tkinter']  # Исключает tkinter, если не нужен
        }
    },
    executables=[
        Executable('TaskerDate.py', base=base, icon='Bokehlicia-Captiva-Office-calendar.ico')
    ]
)


# python setup.py build
