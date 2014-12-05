#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    'sentry>=5.3.3',
    'redis',
]

f = open('README.rst')
readme = f.read()
f.close()

setup(
    name='sentry-redispubsub',
    version='0.0.1',
    author='Anthony Boah',
    author_email='anthony.boah@innogames.com',
    url='https://github.com/innogames/sentry-redispubsub',
    description='A Sentry extension which sends errors to a Redis pub/sub queue',
    long_description=readme,
    license='WTFPL',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=install_requires,
    entry_points={
        'sentry.plugins': [
            'redispubsub = sentry_redispubsub.plugin:RedisPubSubPlugin'
        ],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development'
    ],
    keywords='sentry redis pubsub message queue msg',
)
