import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="super-case-converter-2000",
    version="1.1.2",
    license='GPL v3',
    author="Riccardo Curcio",
    author_email="curcioriccardo@gmail.com",
    description="Case converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RiccardoCurcio/super-case-convertor-2000.git",
    download_url = 'https://github.com/RiccardoCurcio/super-case-convertor-2000/archive/v1.1.2.tar.gz',
    packages=setuptools.find_packages(),
    keywords = [
        'snake',
        'camel',
        'pascal',
        'kebab',
        'flat',
        'raw',
        'path',
        'piped',
        'custom',
        'title'
    ],
    install_requires=['typing'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
