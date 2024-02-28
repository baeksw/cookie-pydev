from setuptools import setup, find_packages

setup(
    name='{{cookiecutter.project_name}}',
    version='1.0.0',  
    packages=find_packages(), 
    include_package_data=True, 
    license='MIT', 
    description='{{cookiecutter.project_name}}',
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown', 
    author='SeungWoo.BAEK', 
    author_email='dohaskell7@gmail.com', 
    url='https://www.example.com/',  
    install_requires=[
        'Django>=3.0',  
        'click>=7.0'
    ],
    entry_points={
        'console_scripts': [
            '{{cookiecutter.project_name}}={{cookiecutter.project_name}}.cli:hello',
            # '명령어=패키지명.모듈명:함수명' 형식으로 여러 CLI 명령어를 정의할 수 있습니다.
        ],    
    },
    classifiers=[ 
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: X.Y',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.X',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires='>3.8',
)