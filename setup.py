from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in accentiqa/__init__.py
from accentiqa import __version__ as version

setup(
	name="accentiqa",
	version=version,
	description="Accentiqa system pvt.ltd",
	author="naresh",
	author_email="nareshgangireddy7167@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
