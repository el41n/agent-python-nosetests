import os

from setuptools import setup


def read_file(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


version = '0.0.1'
tar_url = 'https://github.com/reportportal/agent-python-nosetests'


requirements = [
    'reportportal-client>=3.1.0',
    'nose>=1.3.0',
    'six>=1.10.0',
    'dill>=0.2.7.1',
]


setup(
    name='nose-reportportal',
    version=version,
    description='Agent for Reporting results of tests to the Report Portal',
    long_description=read_file('README.rst'),
    long_description_content_type='text/markdown',
    author='Dzmitry Kolb',
    author_email='dm.kolb@gmail.com',
    url='https://github.com/reportportal/agent-python-nosetests',
    download_url=tar_url,
    packages=['nose_reportportal'],
    install_requires=requirements,
    license='Apache 2.0',
    keywords=['testing', 'reporting', 'reportportal', 'nose'],
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
        ],
    entry_points={
        'nose': [
            'nose_reportportal = nose_reportportal.plugin',
        ]
    },
)
