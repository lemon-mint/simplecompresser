from setuptools import setup, find_packages

setup(
    name             = 'SimpleCodeCompresser',
    version          = '1.0',
    description      = 'Just a simple code compresser',
    author           = 'lemon-mint',
    author_email     = 'ice.lemons.mint@gmail.com',
    url              = 'https://github.com/lemon-mint/simplecompresser',
    download_url     = 'https://github.com/lemon-mint/simplecompresser',
    install_requires = [],
    packages         = find_packages(),
    keywords         = ['compress', 'codedeploy','deploy'],
    python_requires  = '>=3',
    package_data     =  {},
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)