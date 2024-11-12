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
    description='Genome.AI ',
    dependency_links=[
        'https://github.com/PrasenjitGiri/nagarro.git@genome#egg=nagarro',
        'https://github.com/PrasenjitGiri/nagarro.git@genai#egg=nagarro',
        'https://github.com/PrasenjitGiri/nagarro.git@genai#egg=nagarro'
    ]
    
)