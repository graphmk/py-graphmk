import setuptools
import requests
from py_graphmk.version import Version
from os.path import basename, exists, dirname, abspath, join
from setuptools import find_packages


graphmk_version = '1.0.0'
DATAPATH = join(abspath(dirname((__file__))), 'py_graphmk\lib\graphmk-{0}.jar'.format(graphmk_version))

def download_jars(datapath, version=graphmk_version):
    jar_url = 'https://repo1.maven.org/maven2/io/github/graphmk/graphmk/1.0.0/graphmk-{0}.jar'.format(version)
    jar_name = basename(jar_url)
    downloaded_obj = requests.get(jar_url)
    with open(datapath, "wb") as file:
        file.write(downloaded_obj.content)

download_jars(datapath=DATAPATH)

setuptools.setup(
                name='py_graphmk',
                version=Version('1.0.0').number,
                description='Python Wrapper for GraphMk',
                long_description=open('README.rst').read().strip(),
                author='keshan',
                author_email='keshann.18@cse.mrt.ac.lk',
                url='https://github.com/graphmk/py_graphmk',
                py_modules=['py_graphmk/py_graphmk', 'py_graphmk/__init__'],
                data_files=[('py_graphmk/lib', ['py_graphmk/lib/graphmk-{version}.jar'.format(version=graphmk_version)])],
                install_requires=[
                    'pytest',
                    'pytest-cov',
                    'JPype1',
                    'chardet',
                    'requests'
                ],
                license='MIT License',
                zip_safe=False,
                keywords=('graphmk','graph','extraction','analytics','relational','database'),
                classifiers=[       
                    'Development Status :: 5 - Production/Stable',
                    'Environment :: Console',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: Apache Software License',
                    'Operating System :: OS Independent',
                    'Programming Language :: Python :: 2.7',
                    'Natural Language :: English'
                    ]
            )
