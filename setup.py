from setuptools import setup, find_packages

setup(
    name='word-processing-cli',  
    version='0.0.1', 
    description='A CLI that handles text input from either files or file streams. This is a clone of the unix command "wc".',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/7bbg/word-processing-cli',
    packages=find_packages(where='src'),  
    package_dir={'': 'src'},  
    install_requires=[ ],
    entry_points={
        'console_scripts': [
            'wp=src.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)
