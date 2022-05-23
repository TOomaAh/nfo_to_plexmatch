import os
import sys
import xml.etree.ElementTree as ET
from tqdm import tqdm
from file import File
from plexmatch import PlexMatch
from xml import XML

def walk_dir_show(path: str) -> None:
    f = None
    for root, _, files in os.walk(path):
        need_convert = False
        for file in files:
            if "tvshow.nfo" in file:
                need_convert = True
            if ".plexmatch" in file:
                need_convert = False
                break
        if need_convert:
            f = File("tvshow.nfo", root)
            nfoTo_plexmatch(f)

def walk_dir_movie(path: str) -> list:
    bar = tqdm(unit=" folders scanned")
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".nfo") and ".plexmatch" not in file:
                f = File(file, root)
                nfoTo_plexmatch(f)
        bar.update(1)

def write_match(path: str, plex_match: PlexMatch) -> None:
    with open(f"{path}/.plexmatch", "w") as f:
        f.write(plex_match.to_plexmatch())


def nfoTo_plexmatch(nfo_files) -> None:
    xml = XML(f"{nfo_files.path}/{nfo_files.name}")
    xml.parse()
    xml.get_root()

    plexmatch = xml.get_plexmatch()
    write_match(nfo_files.path, plexmatch)


def help():
    print(f"""
    Usage:
        {sys.argv[0]} <option> <path>
    Options:
        -h, --help:
            Print this help message
        -s, --show:
            Convert nfo for shows
        -m, --movie:
            Convert nfo for movies
    """)


if __name__ == "__main__":
    if len(sys.argv) == 1 and sys.argv[1] in ("-h", "--help"):
        help()
        sys.exit(0)

    if len(sys.argv) < 3:
        print(help())
        sys.exit(1)

    nfo_files = []

    if sys.argv[1] in ("-s", "--show"):
        walk_dir_show(sys.argv[2])
        print(nfo_files)
        exit(0)

    if sys.argv[1] in ("-m", "--movie"):
        print(f"Scan movies in {sys.argv[2]}")
        walk_dir_movie(sys.argv[2])
        exit(0)

    print(help())