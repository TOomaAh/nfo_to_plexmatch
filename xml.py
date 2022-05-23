from xml.etree.ElementTree import Element, ElementTree
import xml.etree.ElementTree as ET
from plexmatch import PlexMatch


class XML:

    def __init__(self, filename):
        self.filename = filename
        root = None
        tree = None


    def parse(self) -> ElementTree:
        self.tree = ET.parse(self.filename)

    def get_root(self):
        self.root = self.tree.getroot()

    def get_title(self):
        return self.root.find("title")

    def get_year(self):
        return self.root.find("year")

    def get_tmdbid(self):
        return self.root.find("tmdbid")
    
    def get_imdbid(self):
        return self.root.find("imdb_id")
    
    def get_tvdbid(self):
        return self.root.find("id")
    
    def get_plexmatch(self):
        title = self.get_title()
        year = self.get_year()
        tmdbid = self.get_tmdbid()
        imdbid = self.get_imdbid()
        tvdbid = self.get_tvdbid()

        plex_match = PlexMatch(title, year, tmdbid, imdbid, tvdbid)
        return plex_match

    def __str__(self):
        return f"XML ( filename: {self.filename} )"

    def __repr__(self):
        return f"XML('{self.filename}')"
