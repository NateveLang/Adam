version = '0.0.1'

import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding = 'utf-8') # Get the long description from the README file

setup(
	name = 'nateve-adam',
	packages = ['nateve-adam'],
	version = version,
	license='MIT',
	description = 'Nateve transpiler developed with python 3.8',
	author = 'Emmanuel Norambuena',
	author_email = 'eanorambuena@uc.cl',
	long_description = long_description,
	long_description_content_type = 'text/markdown',

	url = 'https://github.com/NateveLang/Adam',
	download_url = f'https://github.com/NateveLang/Adam/archive/v{version}.tar.gz',
	keywords = "development, quantum computing, programming language, nateve, natevelang, nate, education".split(", "),
	
	install_requires = [
		'eggdriver',
		'qiskit',
	],

	packages = find_packages(),
	python_requires = '>=3.5, <=3.8',

	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
	],

	project_urls = {
		'Bug Reports': 'https://github.com/NateveLang/Adam/issues',
		'Source': 'https://github.com/NateveLang/Adam',
	},
)