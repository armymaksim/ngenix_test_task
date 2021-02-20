from typing import List, Tuple
from xml.etree import ElementTree as et
from xml.etree.ElementTree import tostring

from .constants import (
    TAG_ROOT,
    TAG_VAR,
    ATTR_NAME,
    ID,
    ATTR_VALUE,
    LEVEL,
    TAG_OBJECTS,
    TAG_OBJECT
)
from .file_structure import XMLFileStructure


def generate_xml() -> bytes:
    obj = XMLFileStructure()
    root = et.Element(TAG_ROOT)
    et.SubElement(
        root,
        TAG_VAR,
        {
            ATTR_NAME: ID,
            ATTR_VALUE: obj.tag_id
         }
    )
    et.SubElement(
        root,
        TAG_VAR,
        {
            ATTR_NAME: LEVEL,
            ATTR_VALUE: str(obj.tag_level)
        }
    )
    objects = et.SubElement(
        root,
        TAG_OBJECTS
    )

    for obj_name in obj.object_names:
        et.SubElement(
            objects,
            TAG_OBJECT,
            {ATTR_NAME: obj_name}
        )

    return tostring(root)


def parse_xml(xmlstring: str) -> XMLFileStructure:
    tree = et.ElementTree(et.fromstring(xmlstring))
    root = tree.getroot()
    attr_id, attr_level = _parse_vars(root.findall(TAG_VAR))
    objects = _parse_objects(
        root.find(TAG_OBJECTS).findall(TAG_OBJECT)
    )
    return XMLFileStructure(
        tag_id=attr_id,
        tag_level=attr_level,
        object_names=objects,
    )


def _parse_vars(vars: List[et.Element]) -> Tuple[str, int]:
    attr_id = attr_level = None
    for var in vars:
        if var.get(ATTR_NAME) == ID:
            attr_id = var.get(ATTR_VALUE)
            continue

        if var.get(ATTR_NAME) == LEVEL:
            attr_level = var.get(ATTR_VALUE)
            if not str.isdigit(attr_level):
                raise ValueError('attr_level must be int')
            continue

    return attr_id, int(attr_level)


def _parse_objects(objects: List[et.Element]) -> List[str]:
    return [
        el.get(ATTR_NAME)
        for el in objects
    ]
