from setuptools import setup, find_packages

setup(
    name="temporal_abstraction",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.19.0",
        "pandas>=1.0.0",
        "scikit-learn>=0.24.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for temporal abstraction of time series data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/temporal_abstraction",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 