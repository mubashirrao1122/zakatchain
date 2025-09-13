from setuptools import setup, find_packages

setup(
    name='zakat-blockchain-simulation',
    version='0.1.0',
    author='Mubashir Rao',
    author_email='mubashirrao1472@gmail.com',
    description='A simulation of a Zakat Blockchain system for accurate Zakat calculation and transaction history maintenance.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)