from setuptools import setup

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

AUTHORNAME = 'KHANG & DUNGARANI'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.01',
    author = AUTHORNAME,
    author_email= 'khangquang305@gmail.com',
    description= 'A small example package for movies recommendation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package=[SRC_REPO],
    python_requires = '>=3.11'
)