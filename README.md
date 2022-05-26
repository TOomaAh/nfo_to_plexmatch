# nfo_to_plexmatch

A small script that transforms Emby/Jellyfin NFO files into plexmatch.

## dependencies:
`pip install tqdm`

## run

### tvshow

`python nfoToPlexMatcher.py --show "your/path"`

### movie

`python nfoToPlexMatcher.py --movie "your/path"`

## options
```
-h, --help:
    Print this help message
-s, --show: #required
    Convert nfo for shows
-m, --movie: #required
    Convert nfo for movies
-o, --override: #optional (default: False)
    Override existing .plexmatch files
```