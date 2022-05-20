from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lathaniperfumes/__init__.py
from lathaniperfumes import __version__ as version

setup(
	name="lathaniperfumes",
	version=version,
	description="Lathani Perfume in Bahrain",
	author="sammish",
	author_email="sammish.thundiyil@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
