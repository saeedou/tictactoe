from setuptools import setup


PACKAGENAME = 'tictactoe'
dependencies = [
    'easycli'
]


setup(
    name=PACKAGENAME,
    version='0.1.0',
    description='tic tac toe game',
    long_description=open('README.md').read(),
    install_requires=dependencies,
    py_modules=[PACKAGENAME],
    entry_points={
        'console_scripts': [
            'tictactoe = tictactoe:Game.quickstart',
        ]
    }
)
