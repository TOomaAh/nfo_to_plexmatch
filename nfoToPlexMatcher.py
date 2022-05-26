from msilib.schema import Media
import os
import sys
from tqdm import tqdm
from file import File
from movie import Movie
from plexmatch import PlexMatch
from show import Show
from xmlfile import XMLFile


def walk_dir(media: Media, path: str, override: bool = False) -> None:
    bar = tqdm(unit=" folders scanned")
    for root, _, files in os.walk(path):
        need_convert = False
        f = None
        for file in files:
            if media.check_nfo(file):
                f = File(file, root)
                need_convert = True
            if not override and ".plexmatch" in file:
                need_convert = False
                break

        if need_convert:
            nfoTo_plexmatch(f)

        bar.update(1)


def write_match(path: str, plex_match: PlexMatch) -> bool:
    with open(f"{path}/.plexmatch", "w", encoding="utf-8") as f:
        try:
            f.write(plex_match.to_plexmatch())
            return True
        except Exception:
            return False


def nfoTo_plexmatch(nfo_files) -> bool:
    xml = XMLFile(f"{nfo_files.path}/{nfo_files.name}")
    if not xml.parse():
        return False
    xml.get_root()

    plexmatch = xml.get_plexmatch()
    write_match(nfo_files.path, plexmatch)
    return True


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
        -o, --override:
            Override existing .plexmatch files
    """)


if __name__ == "__main__":

    path = sys.argv[len(sys.argv) - 1]
    if (path.startswith("--")):
        print("Not Path specified")
        print(help())
        exit(1)

    is_movie = False
    override = False

    for i in sys.argv:
        if i == "-h" or i == "--help":
            help()
            exit(0)
        if (i == "--show" or i == "-s"):
            is_movie = False
        if (i == "--movie" or i == "-m"):
            is_movie = True
        if (i == "--override" or i == "-o"):
            override = True


    if is_movie:
        walk_dir(Movie(), sys.argv[len(sys.argv) - 1], override)
    else:
        walk_dir(Show(), sys.argv[len(sys.argv) - 1], override)