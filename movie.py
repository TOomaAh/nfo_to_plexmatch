from media import Media


class Movie(Media):

    def __init__(self) -> None:
        super().__init__()

    def check_nfo(self, file: str) -> bool:
        if file.endswith(".nfo"):
            return True
        return False