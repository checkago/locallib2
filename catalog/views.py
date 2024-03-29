from django.shortcuts import render
from .models import Book, Author, Chapter
from django.views import generic


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    # Доступные книги (статус = 'a')
    num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_authors': num_authors},
    )


class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, pk):
        try:
            book_id = Book.objects.get(pk=pk)
            chapters = Chapter.objects.set(pk=pk)

        except Book.DoesNotExist:
            raise Http404("Книги в каталоге нет")

        return render(
            request,
            'catalog/book_detail.html',
            context={'book': book_id, 'chapters': chapters, 'text': text}
        )


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, pk):
        try:
            author_id = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404("Книги в каталоге нет")

        # author_id=get_object_or_404(Author, pk=pk)

        return render(
            request,
            'catalog/author_detail.html',
            context={'author': author_id, }
        )


class ChapterListView(generic.ListView):
    model = Chapter


class ChapterDetailView(generic.DetailView):
    model = Chapter

    def chapter_detail_view(request, pk):
        try:
            chapter_id = Chapter.objects.get(pk=pk)
        except Chapter.DoesNotExist:
            raise Http404("Главы в книге")

        # book_id=get_object_or_404(Book, pk=pk