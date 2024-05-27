import pytest
from book import Book

@pytest.mark.parametrize('title, isbn', [
    ('Animal Stories', '978-1-60309-502-0'),
    ('Ashes', '978-1-60309-517-4'),
    ('But You Have Friends', '978-1 60309-527-3')
])
def test_valid_creation(title, isbn):
    assert Book(title, isbn), f'Book should be valid'
    
@pytest.mark.parametrize('title, isbn', [
    ('', '978-1-60309-502-0'),
    ('', '978-1-60309-517-4'),
    ('', '978-1-60309-527-3')
])
def test_creation_with_invalid_title(title, isbn):
    with pytest.raises(RuntimeError) as error:
        Book(title, isbn)
    assert error, f'Should raise RuntimeError for invalid title.'
    
@pytest.mark.parametrize('title, isbn', [
    ('Animal Stories', '978-1-60309-4502-0'),
    ('Ashes', '978-1-60309-518-4'),
    ('But You Have Friends', '978-1 90309-527-3')
])
def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError) as error:
        Book(title, isbn)
    assert error, f'Should raise RuntimeError for invalid isbn.'