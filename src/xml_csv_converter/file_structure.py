import string
from dataclasses import dataclass, field
from random import randint, choice
from typing import List
from uuid import uuid4

from .constants import LEVEL_RANGE, RND_STR_LEN_RANGE, OBJECTS_COUNT_RANGE


def random_str() -> str:
    return ''.join(
        choice(string.ascii_letters + string.digits)
        for _ in range(randint(*RND_STR_LEN_RANGE))
    )


def random_unique_str() -> str:
    return f'{uuid4().hex}{random_str()}'


def level_generator() -> int:
    return randint(*LEVEL_RANGE)


def objects_generator() -> List[str]:
    return [
        random_str() for _ in range(randint(*OBJECTS_COUNT_RANGE))
    ]


@dataclass(frozen=True)
class XMLFileStructure:
    tag_id: str = field(default_factory=random_unique_str, init=True)
    tag_level: int = field(default_factory=level_generator, init=True)
    object_names: List[str] = field(
        default_factory=objects_generator,
        init=True
    )
