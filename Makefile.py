import setuptools

setuptools.setup(
    name='im2a',
    version='.3',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
