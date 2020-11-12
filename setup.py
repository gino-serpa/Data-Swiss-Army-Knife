import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dasak", # Replace with your own username
    version="0.0.1",
    author="Gino Serpa",
    author_email="gino.serpa@gmail.com",
    description=long_description,
    long_description="Data Analytics Swiss Army Knife",
    long_description_content_type="text/markdown",
    url="https://github.com/gino-serpa/Data-Swiss-Army-Knife",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
