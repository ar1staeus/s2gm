# s2gm

Simple Python3 script to convert Spotify playlists to Play music playlists. Intended for use with free Play music accounts, so the script will only attempt to use songs in the user's library. Uses [Spotipy](https://github.com/plamere/spotipy) and [gmusicapi](https://github.com/plamere/spotipy).

## Usage

```
s2gm [-h] --email EMAIL --password PASSWORD --spotifyuser SPOTIFYUSER
            [--name NAME] [--skip]
            uri

positional arguments:
  uri

optional arguments:
  -h, --help            show this help message and exit
  --email EMAIL         Google username
  --password PASSWORD   Google password
  --spotifyuser SPOTIFYUSER
                        Spotify username
  --name NAME           Name to assign to the resulting playlist. If blank,
                        the Spotify playlist name will be used
  --skip                Skip missing songs
```

For example:

```
s2gm --email example@example.com --password pass123 --spotifyuser exampleuser spotify:user:spotify:playlist:3OyvSycblmE3oPeY5rcqNe
```

Please note that because of limitations on the [Spotipy](https://github.com/plamere/spotipy) API, you need to be following or own the playlist in order to access its data.

## Installation

Dependencies:

- Spotipy
- gmusicapi
- termcolor

Install with Python distutils:

```
git clone https://github.com/stephanlensky/s2gm.git && cd s2gm
python setup.py sdist && cd dist
tar -xvf * && cd *
sudo python setup.py install
```
