from setuptools import setup, find_packages

setup(
    name='tamnun',
    packages=find_packages(exclude=['test*']),
    install_requires=[
        'numpy==1.15.4',
        'scikit-learn==0.20.2',
        'torch==1.1.0',
        'pytorch-transformers',
    ]
)
