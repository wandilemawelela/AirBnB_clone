"""
This module initializes the storage for serializing and deserializing objects.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
