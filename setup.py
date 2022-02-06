import setuptools

# Read README.md as a variable to pass as the package's long
# description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='bl-bfg',
    version='0.1',
    author='Justin Angel',
    author_email='justin@arch4ngel.ninja',
    description='A simple password guessing framework.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/arch4ngel/bl-bfg',
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.7',
    install_requires=['requests_ntlm',
        'bruteloops',
        'pysmb==1.1.27']
)