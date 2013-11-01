import os
import importlib

__all__ = []
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or not module.endswith('.py'):
        continue

    importlib.import_module('.' + module[:-3], __name__)

del module
