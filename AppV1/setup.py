from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('app.py', base=base, target_name = 'AppV1')
]

setup(name='App Version 1',
      version = '1',
      description = 'Original App',
      options = {'build_exe': build_options},
      executables = executables)
