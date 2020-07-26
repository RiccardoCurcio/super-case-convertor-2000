import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="super-case-converter",
    version="0.0.1",
    author="Riccardo Curcio",
    author_email="curcioriccardo@gmail.com",
    description="Case converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RiccardoCurcio/super-case-convertor-2000.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL v3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
