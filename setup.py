from setuptools import setup

setup(
    name='s2gm',
    version='0.1',
    description='Tries to convert a user\'s Spotify playlist to a Play music playlist with only songs in that user\'s library.',
    url='https://github.com/ar1staeus/s2gm',
    author='Stephan Lensky',
    author_email='stephan.lensky@gmail.com',
    license='MIT',
    scripts=['s2gm'],
    install_requires=[
        'spotipy',
        'gmusicapi',
        'termcolor'
    ]
)