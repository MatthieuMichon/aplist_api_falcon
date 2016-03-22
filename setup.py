"""Airport List Query web-API for Falcon WSGI Server module.

See:
https://github.com/MatthieuMichon/aplist_api_falcon
"""

from setuptools import setup

setup(
    name='aplist_api_falcon',
    version='0.1.dev1',
    description='Airport List Query web-API for Falcon WSGI Server module',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
    ],
    url='https://github.com/MatthieuMichon/aplist_api_falcon',
    author='Matthieu Michon',
    author_email='matthieu.michon@gmail.com',
    license='GPLv3',
    packages=['aplist_api_falcon'],
    install_requires=[
          'requests',
          'aplist',
          'falcon',
          'gunicorn',
    ],
    test_suite='tests',
    zip_safe=False
)
