#!/usr/bin/env python3
import os, setuptools

setup_path = os.path.dirname(__file__)

with open(os.path.join(setup_path, "README.md")) as readme:
    long_description = readme.read()

setuptools.setup(
    name="crawler-treadsreddit",
    version="0.1",
    author="Cesar Augusto",
    author_email="cesarabruschetta@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="2-clause BSD",
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests", "docs"]
    ),
    include_package_data=False,
    python_requires=">=3.7",
    install_requires=["requests", "beautifulsoup4", "python-telegram-bot"],
    test_suite="tests",
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Other Environment",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ),
    entry_points="""\
        [console_scripts]
            threadsreddit=threads_reddit.main:main
    """,
)
