import os
import sys
from tqdm import tqdm
from file import File
from plexmatch import PlexMatch
from xmlfile import XMLFile

def walk_dir_show(path: str, override: bool = False) -> None:
    f = None
    for root, _, files in os.walk(path):
        need_convert = False
        for file in files:
            if "tvshow.nfo" in file:
                need_convert = True
            if ".plexmatch" in file:
                need_convert = False
                break
        if need_convert or override:
            f = File("tvshow.nfo", root)
            nfoTo_plexmatch(f)

def walk_dir_movie(path: str, override: bool = False) -> list:
    error = []
    bar = tqdm(unit=" folders scanned")
    for root, dirs, files in os.walk(path):
        need_convert = False
        current_nfo = None
        for file in files:
            if file.endswith(".nfo"):
                f = File(file, root)
                current_nfo = f
                need_convert = True

            if not override and ".plexmatch" in file:
                need_convert = False
                break

        if need_convert:
            nfoTo_plexmatch(current_nfo, error)

        bar.update(1)

    if len(error) > 0:
        print("\n\n")
        print("Error:")
        for e in error:
            print(f"{e}")


def write_match(path: str, plex_match: PlexMatch) -> None:
    with open(f"{path}/.plexmatch", "w", encoding="utf-8") as f:
        try:
            f.write(plex_match.to_plexmatch())
        except Exception as e:
            print(f"Cannot create file in {path}")


def nfoTo_plexmatch(nfo_files, error: list) -> None:
    xml = XMLFile(f"{nfo_files.path}/{nfo_files.name}")
    if not xml.parse():
        error.append(nfo_files)
        return
    xml.get_root()

    plexmatch = xml.get_plexmatch()
    #print(plexmatch.to_plexmatch())
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
        -o, --override:
            Override existing .plexmatch files
    """)


if __name__ == "__main__":
    if len(sys.argv) == 1 and sys.argv[1] in ("-h", "--help"):
        help()
        sys.exit(0)

    path = sys.argv[len(sys.argv) - 1]
    if (path.startswith("--")):
        print("Not Path specified")
        print(help())
        exit(1)

    is_movie = False
    override = False

    for i in sys.argv:
        if (i == "--show" or i == "-s"):
            is_movie = False
        if (i == "--movie" or i == "-m"):
            is_movie = True
        if (i == "--override" or i == "-o"):
            override = True


    if is_movie:
        walk_dir_movie(sys.argv[len(sys.argv) - 1], override)
    else:
        walk_dir_show(sys.argv[len(sys.argv) - 1], override)


    print(help())