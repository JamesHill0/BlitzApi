from setuptools import setup, find_packages

setup(
    name='BlitzApi',
    version='0.1.0',
    packages=find_packages(),
    description='A simple Blitz API for pub/sub, scraping, and user management',
    author='James Hill',
    author_email='jameshill@example.com',
    url='https://github.com/jameshill/BlitzApi',
    install_requires=[
        # Add your package dependencies here
        'paho-mqtt',
        'requests',  # Assuming the scraper might need requests
    ],
)
