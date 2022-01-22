from setuptools import setup

setup(
    name='mp3_utils',
    version='0.0.1',
    description='My private package from private github repo',
    url='git@github.com:mizumizuu/mp3-utils.git',
    author='John Doe',
    author_email='onlyaforapple@gmail.com',
    license='unlicense',
    install_requires=["requests-html"],
    packages=['mp3_utils'],
    zip_safe=False
)
