import os
from setuptools import setup

def read(file):
    return open(os.path.join(os.path.dirname(__file__), file)).read()

setup(
    name="vsut",
    version="1.6",
    author="Alex Egger",
    author_email="alex.egger96@gmail.com",
    description="A simple unit testing framework for Python 3.4",
    license="MIT",
    keywords="unit unittest test testing",
    url="http://github.com/zillolo/vsut-python",
    packages=["vsut"],
    scripts=["runner.py"],
    entry_points = {"console_scripts" : ["vrun = runner:main"]},
    long_description="""For usage information visit:
    http://github.com/zillolo/vsut-python
""",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing"]
)
