#!/usr/bin/python3
"""This module contains a function for CLI JSON file writing"""
import sys

load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file


def add_to_json(obj):
    """Adds obj to a JSON file

    Args:
        obj (list): Object to append
    """
    li = []
    json_file = 'add_item.json'
    try:
        f = open(json_file, 'x', encoding='utf-8')
        f.close()
    except Exception:
        li = load(json_file)
    finally:
        li += (obj)
        save(li, json_file)


if __name__ == "__main__":
    args = sys.argv[1:]
    add_to_json(args)
