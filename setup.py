from setuptools import setup, find_packages

setup(
    name='genome',
    version='0.0.1',
    packages=find_packages(
        include=[
            'nagarro.genome',
            'nagarro.genome.*',
            'nagarro.genome.genai',
            'nagarro.genome.genai.*',
            'nagarro.genome.mlops',
            'nagarro.genome.mlops.*'
            ]),
    install_requires=[
        'pandas>=1.3.0'
        ],
    extra_requires={
        'genome':[
            'https://github.com/PrasenjitGiri/nagarro.git@genome#egg=nagarro'
        ],
        'genai':[
            'https://github.com/PrasenjitGiri/nagarro.git@genai#egg=nagarro'
        ],
        'mlops':[
            'https://github.com/PrasenjitGiri/nagarro.git@genai#egg=nagarro'
        ]
    },
    include_package_data=True,
    description='Genome.AI ',
    dependency_links=[
        'https://github.com/PrasenjitGiri/nagarro.git@genome#egg=nagarro',
        'https://github.com/PrasenjitGiri/nagarro.git@genai#egg=nagarro',
        'https://github.com/PrasenjitGiri/nagarro.git@genai#egg=nagarro'
    ]
    
)