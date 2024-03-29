# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open("README.md","r",encoding="utf-8-sig") as f:
    readme = f.read()

with open("requirements.txt","r",encoding="utf-8-sig") as f:
    requirements = [i.strip() for i in f.readlines()]

setup(
    name="PyThaiOCR",
    version="0.1dev0",
    description="Python Thai OCR",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Wannaphong",
    author_email="wannaphong@yahoo.com",
    url="https://github.com/wannaphong/pythaiocr",
    packages=find_packages(),
    test_suite="tests",
    python_requires=">=3.6",
    # package_data={
    #     "laonlp": [
    #         "corpus/*",
    #     ]
    # },
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords=[
        "lao",
        "Thai",
        "natural language processing",
        "text analytics",
        "text processing",
        "localization",
        "computational linguistics",
        "Thai language",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Linguistic",
    ],
    project_urls={
        "Documentation": "https://github.com/wannaphong/pythaiocr/wiki",
        "Source": "https://github.com/wannaphong/pythaiocr",
        "Bug Reports": "https://github.com/wannaphong/pythaiocr/issues",
    },
)
