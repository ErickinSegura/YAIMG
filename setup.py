from setuptools import setup, find_packages
import re

def get_version():
    try:
        with open("yaimg/__version__.py") as f:
            version_file = f.read()
            version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
            if version_match:
                return version_match.group(1)
            raise RuntimeError("Unable to find version string.")
    except FileNotFoundError:
        raise RuntimeError("Version file not found.")

setup(
    name='yaimg',
    version=get_version(),
    packages=find_packages(),
    install_requires=[
        'Pillow>=8.0.1',
    ],
    entry_points={
        'console_scripts': [
            'yaimg = yaimg.cli:main',
        ],
    },
    author='ErickInSegura',
    description='Herramienta de compresión de imágenes desde terminal',
    keywords='image compression cli',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)