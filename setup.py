from setuptools import setup, find_packages

setup(
    name="news_scraper",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests==2.31.0",
    ],
    python_requires=">=3.6",
) 