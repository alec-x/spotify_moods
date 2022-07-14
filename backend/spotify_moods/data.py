from dataclasses import dataclass

@dataclass
class spotify_image:
    height: int
    width: int
    url: str

@dataclass
class spotify_album():
    id: str
    name: str
    artists: list[str]
    href: str
    images: list[spotify_image]


@dataclass
class spotify_song():
    id: str
    name: str
    artists: list[str]
    album: str # album ID
    href: str
    uri: str
    images: list[spotify_image]