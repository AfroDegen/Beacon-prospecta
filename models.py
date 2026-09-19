from dataclasses import dataclass


@dataclass
class Agency:
    name: str
    website: str
    location: str
    category: str
    source: str


@dataclass
class Client:
    name: str
    source_page: str


@dataclass
class BenchmarkCandidate:
    agency: Agency
    client: Client
    confidence: int
