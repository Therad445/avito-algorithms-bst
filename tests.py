import subprocess
import sys
from pathlib import Path


file = Path(__file__).with_name('main.py')


def check(cmds, expected):
    s = str(len(cmds)) + '\n' + '\n'.join(cmds) + '\n'
    p = subprocess.run([sys.executable, str(file)], input=s,
                       text=True, capture_output=True, check=True)
    got = p.stdout.strip().splitlines()
    assert got == expected, f'expected {expected}, got {got}'


check([
    'root', 'height', 'print', 'exists 4', 'next 4', 'prev 4',
    'add 4', 'root', 'height', 'print'
], ['Empty', '0', 'Empty', 'NO', 'None', 'None', '4', '1', '4'])

check([
    'add 3', 'add 2', 'add 1', 'root', 'height', 'print',
    'add 2', 'exists 2', 'del 8', 'print'
], ['2', '2', '2 1 3', 'YES', '2 1 3'])

check([
    'add 1', 'add 3', 'add 2', 'root', 'print', 'del 1',
    'root', 'height', 'add -5', 'root', 'print'
], ['2', '2 1 3', '2', '2', '2', '2 -5 3'])

check([
    'add 30', 'add 20', 'add 10', 'add 25', 'add 40',
    'del 20', 'root', 'print', 'exists 20', 'next 26', 'prev 26'
], ['25', '25 10 30 40', 'NO', '30', '25'])

check([
    'add -5', 'add 0', 'add 9', 'next -5', 'prev 0',
    'next 1', 'prev -6', 'next 10', 'del 0', 'exists 0'
], ['-5', '0', '9', 'None', 'None', 'NO'])

print('OK')
