#!/usr/bin/env python
'''
A CLI front-end to a running salt-api system

'''
from distutils.core import setup

salt_version = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'salt', 'version.py')

exec(compile(open(salt_version).read(), salt_version, 'exec'))

setup_kwargs = {
    'name': 'pepper',
    'version': __version__,
    'description': __doc__,
    'author': 'Thomas S Hatch',
    'author_email': 'thatch45@gmail.com',
    'url': 'http://saltstack.org',
    'classifiers': [
        'Programming Language :: Python',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Clustering',
        'Topic :: System :: Distributed Computing',
    ],
    'packages': [
        'pepper',
    ],
    'data_files': [
        ('share/man/man1', ['doc/man/pepper.1']),
    ],
    'scripts': [
        'scripts/pepper'
    ],
}

if __name__ == '__main__':
    setup(**setup_kwargs)
