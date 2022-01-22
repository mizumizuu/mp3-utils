from setuptools import setup

setup(
    name='mp3_downloader',
    version='0.0.1',
    description='My private package from private github repo',
    url='git@github.com:mizumizuu/mp3-downloader.git',
    author='John Doe',
    author_email='onlyaforapple@gmail.com',
    license='unlicense',
    install_requires=["python-dotenv", "requests-html"],
    packages=['mp3_downloader'],
    zip_safe=False
)
