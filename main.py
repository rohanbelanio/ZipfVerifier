import gutenbergpy.textget
from gutenbergpy.gutenbergcache import GutenbergCache
import random

if not GutenbergCache.exists():
    GutenbergCache.create(refresh=True, download=True, unpack=True, parse=True, cache=True, deleteTemp=True)

cache = GutenbergCache.get_cache()

books_herman_melville = cache.query(authors=['Orwell, George'])


for book in books_herman_melville:
    gutenbergpy.textget.get_text_by_id(book)