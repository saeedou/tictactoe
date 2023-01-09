from setuptools import setup


PACKAGENAME = 'tictactoe'
dependencies = [
    'easycli'
]


setup(
    name=PACKAGENAME,
    version= '0.1',
    description='tic tac toe game',
    long_description=open('README.md').read(),
    install_requires=dependencies,
    py_modules=[PACKAGENAME],

)
