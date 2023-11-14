# config/utils.py
from django.core.cache.backends.base import BaseCache


class NoCacheStorage(BaseCache):
    def add(self, *args, **kwargs):
        return True

    def get(self, *args, **kwargs):
        return None

    def set(self, *args, **kwargs):
        return True

    def delete(self, *args, **kwargs):
        return True
