from setuptools import setup, find_packages

setup(
    name='ipynb-function',
    version='0.1',
    description='Package / Module importer for importing code from Jupyter Notebook files (.ipynb)',
    url='http://github.com/yuvipanda/ipynb',
    author='Yuvi Panda, Jiaming Lu',
    author_email='yuvipanda@gmail.com;jiaminglu@live.com',
    license='BSD',
    packages=find_packages(),
    python_requires='>=3.4'
)
