from setuptools import setup

with open('saturn/version.py') as f:
    __version__ = f.read().split("=", 1)[1].strip()


setup(
    name='saturn',
    version=__version__,
    description="Saturn allows to rerun python scripts skipping some places that were defined in previous runs.",
    author='Alexander Khlebushchev',
    packages=[
        'saturn',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': ['saturn=saturn.terminal:main'],
    },
)
