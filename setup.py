from setuptools import setup, find_packages
from os.path import join, dirname
import mouse_control
setup(
    name='mouse_control',
    version=mouse_control.__version__,
    author='',
    author_email='',
    packages=find_packages(),
    url='',
    description='',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    keywords='',
    entry_points={
        'console_scripts':
            ['run = mouse_control.control:get_position']
    },
    install_requires=[
        'tk-tools==0.13.0',
        'pyautogui==0.9.50',
        'pynput==1.6.8',
    ],
    include_package_data=True,
)
