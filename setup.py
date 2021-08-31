"""Setup script."""

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    line.strip()
    for line in open(os.path.join(here, "requirements.txt"), "r").readlines()
]

setup(
    name="kode",
    version="20210901",
    description="Kashif code package.",
    long_description="Different code modules commonly used.",
    classifiers=["Programming Language :: Python"],
    author="Kashif Iftikhar",
    author_email="kashif@compulife.com.pk",
    url="https://github.com/kashifpk/kode",
    keywords="Kashif Code Package",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    # entry_points={'console_scripts': ['we = we.we_cmd:cli']},
)
