class PlexMatch:

    def __init__(self, title: str, year: str, tmdb_id: str, imdb_id: str, tvdb_id: str) -> None:
        self.title = title
        self.year = year
        self.tmdb_id = tmdb_id
        self.imdb_id = imdb_id
        self.tvdb_id = tvdb_id

    def to_plexmatch(self) -> str:
        text = f"Title: {self.title}\n"
        if self.year:
            text += f"Year: {self.year}\n"
        if self.tmdb_id:
            text += f"tmdbid: {self.tmdb_id}\n"
        if self.imdb_id:
            text += f"imdbid: {self.imdb_id}\n"
        if self.tvdb_id:
            text += f"tvdbid: {self.tvdb_id}\n"
        return text

    def __str__(self) -> str:
        return f"{self.title} ({self.year})"