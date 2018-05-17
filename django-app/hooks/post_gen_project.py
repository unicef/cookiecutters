import sys
import subprocess

# print __file__
# print os.getcwd()

run_thru_shell = sys.platform.startswith('win')

proc = subprocess.Popen(['python', 'manage.py', 'makemigrations',
                         '{{cookiecutter.package_name}}'], shell=run_thru_shell)
proc.wait()

proc = subprocess.Popen(['git', 'init'], shell=run_thru_shell)
proc.wait()

proc = subprocess.Popen(['git', 'flow', 'init', '-d'], shell=run_thru_shell)
proc.wait()

proc = subprocess.Popen(['pip', 'install', 'pip-tools'], shell=run_thru_shell)
proc.wait()

proc = subprocess.Popen(['make', 'compile-requirements'], shell=run_thru_shell)
proc.wait()
