import pytest
from django.contrib.auth import get_user_model
from django.test.client import Client
from books.models import Book
User = get_user_model()


def test_is_it_working():
    assert True == 1

#def test_should_fail():
#    assert True == False

def test_even_number():
    number = 10
    assert number%2 == 0

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(
        username="test123",
        password="password123"
    )
    assert user.username == "test123"
    assert user.check_password("password123")

# fixture

@pytest.fixture
def user(db) -> User:
    u = User.objects.create_user(
        username="test123",
        password="password123"
    )
    return u


@pytest.fixture
def logged_in_client(user, client: Client) -> Client:
    #cream un browser simulat, logat, care poate face requesturi http
    client.login(
        username="test123",
        password="password123"
    )
    return client

@pytest.fixture
def book(user):
    b = Book.objects.create(title="testbook", author= "Rowling", user= user)
    return b


def test_list_all_books(logged_in_client):
    # making a http get request
    response = logged_in_client.get("/")

    assert response.status_code == 200


def test_does_book_exist(logged_in_client, book):
    # making a http get request
    response = logged_in_client.get("/")

    assert response.status_code == 200
    assert "testbook" in str(response.content)


def test_user_book_count(user):
    book1 = Book.objects.create(title="book 1", author= "author 1", user= user)
    book2 = Book.objects.create(title="book 2", author= "author 2", user= user)
    books = list(Book.objects.filter(user_id=user.pk))
    assert len(books) == 2


def test_user_book_count_html(user, client: Client):
    book1 = Book.objects.create(title="book 1", author="author 1", user=user)
    book2 = Book.objects.create(title="book 2", author="author 2", user=user)
    book3 = Book.objects.create(title="book 3", author="author 3", user=user)

    response = client.get("/")
    assert response.status_code == 200
    main_page_text = str(response.content)
    # /user/1/books/
    assert main_page_text.count(f"/user/{user.pk}/books/") == 3


def test_delete_book(user, book, logged_in_client):
    response = logged_in_client.post(f"/delete_book/{book.pk}/")
    assert response.status_code == 302

    response = logged_in_client.post(f"/delete_book/{book.pk}/")
    assert response.status_code == 404








