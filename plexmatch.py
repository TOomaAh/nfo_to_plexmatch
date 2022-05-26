class PlexMatch:

    def __init__(self, title: str, year: str, tmdb_id: str, imdb_id: str, tvdb_id: str) -> None:
        self.title = title
        self.year = year
        self.tmdb_id = tmdb_id
        self.imdb_id = imdb_id
        self.tvdb_id = tvdb_id

    def to_plexmatch(self) -> str:
        text = f"Title: {self.title.text}\n"
        if self.year is not None:
            text += f"Year: {self.year.text}\n"
        if self.tmdb_id is not None:
            text += f"tmdbid: {self.tmdb_id.text}\n"
        if self.imdb_id is not None:
            text += f"imdbid: {self.imdb_id.text}\n"
        if self.tvdb_id is not None and not self.tvdb_id.text.startswith("tt"):
            text += f"tvdbid: {self.tvdb_id.text}\n"
        return text

    def __str__(self) -> str:
        return f"{self.title} ({self.year})"