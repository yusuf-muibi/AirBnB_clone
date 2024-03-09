#!/usr/bin/python3
"""the __init__ is the magic method for models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
