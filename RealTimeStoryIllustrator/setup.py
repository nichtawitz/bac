from setuptools import setup, find_packages, Command 
 
setup( 
    name='RealTimeStoryIllustrator', 
    version='0.2',
    packages=find_packages(), 
    include_package_data=True, 
    package_data={'rtsi.data': ['*.txt','*.png','*.jpg']}, 
    url='https://github.com/nichtawitz/bac', 
    license='', 
    author='hoebartNichtawitz', 
    author_email='', 
    description='Real Time Story Illustrator - Narrates german stories and displays fitting images', 
    install_requires=[ 
        'gTTs', 
        'PySide', 
        'mstranslator',
        'regex',
        'bing_search_api'
    ], 
    entry_points={ 
        'console_scripts': [ 
            'start_rtsi = rtsi.main:main', 
        ] 
    } 
) 
