#!/usr/bin/env python3


from setuptools import setup


setup(name='youtube_watcher',
        version='0.1b',
        description='A simple program to list new vidoes and download them',
        author='Steven J. Core',
        author_email='42Echo6Alpha@gmail.com',
        license='GPL',
        packages=['youtube_watcher'],
        zip_safe=False,
        include_package_data=True,
        install_requires=[
            'bs4',
            'youtube-dl'
            ],
        entry_points={
            'console_scripts': [
                'youtube_watcher = youtube_watcher.__init__:main'
                ]
            })