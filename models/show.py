from models.media import Media


class Show(Media):

    def __init__(self) -> None:
        super().__init__()

    def check_nfo(self, file: str) -> bool:
        if "tvshow.nfo" in file:
            return True
        return False