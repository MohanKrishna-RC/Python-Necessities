import setuptools

"""
We're importing setuptools which is the standard library used by python,
for building scripts.
Next we can call the setup function of setuptools and pass in the 
required parameters. """

setuptools.setup(
    name='caser',
    version='1.0',
    author='mohan',
    author_email='mk',
    description='Hides a message with a caser cipher',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'caser = caser.caser:main'
        ]

    },
    classifiers=[
        'Programming Language : : Python : : 3',
        'Licence : : OSI Approved : : MIT License',
        'Operating System : : OS Independent',
    ],
)


""" Basically how to interact with your script. Here we are configuring the command caser to be related to our "main"
        function. When we execute our setup.py file it shoulf build and install our script and allow us to
        access it using the caser command. """