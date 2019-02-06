from setuptools import setup

setup(name='ohno',
      version='1.0',
      description='',
      author='!(spandan ke deewane) anymore',
      license='MIT',
      packages=['ohno'],
      install_requires=[
		'beautifulsoup4==4.7.1',
            'certifi==2018.11.29',
            'chardet==3.0.4',
            'EasyProcess==0.2.5',
            'idna==2.8',
            'lxml==4.3.0',
            'python-dateutil==2.7.5',
            'PyVirtualDisplay==0.2.1',
            'requests==2.21.0',
            'selenium==3.141.0',
            'six==1.12.0',
            'soupsieve==1.6.2',
            'urllib3==1.24.1',
            'pyxhook==1.0.0',
            'python-xlib==0.23'
      ],
      entry_points={"console_scripts": ["ohno = ohno:entry", "cprog = ohno:centry", "todo = ohno:tentry"]},
      zip_safe=False)