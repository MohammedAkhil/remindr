import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('remindr/remindr.py').read(),
    re.M
).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name="taskyy",
    packages=["remindr"],
    entry_points={
        "console_scripts": ['taskyy = remindr.remindr:main']
    },
    install_requires=[
        'click',
        'parsedatetime',
        'tinydb',
        'python-crontab'
    ],
    version=version,
    description="Taskyy is a command-line app for you remainders for mac.",
    long_description=long_descr,
    author="Mohammed Akhil",
    author_email="akhilmohammed05@gmail.com",
    url="https://github.com/MohammedAkhil",
)
