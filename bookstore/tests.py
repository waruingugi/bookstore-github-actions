from django.test import TestCase
import random

from bookstore.models import Author, Book
from bookstore.utils import cache_all_books, get_cached_books


class TestCacheSystem(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.author_1 = Author.objects.create(first_name='Ehsan', last_name='Movaffagh')
        cls.author_2 = Author.objects.create(first_name='Ehsan', last_name='Movaffagh')
        authors = [cls.author_1, cls.author_2]

        cls.books = Book.objects.bulk_create([
            Book(name=f'number {_}', author=random.choice(authors)) for _ in range(10000)
        ])

    def test_cached_books(self):
        initial_book_ids = [_.id for _ in self.books]

        cache_all_books()
        cached_books = get_cached_books()
        cached_book_ids = [_['id'] for _ in cached_books]

        self.assertListEqual(initial_book_ids, cached_book_ids)
