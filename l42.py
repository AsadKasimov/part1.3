def make_title(fn):
    def wrapped():
        title = fn()
        title = title.capitalize()
        title = title.replace(',', '')
        return title

    return wrapped


@make_title
def hi():
    return 'hello, world'


print(hi())

# есть функция и нужно ее при необходимости видоизменять то можно использовать декоратор.
# в верху функции просто указываем через @ функцию и она видоизменяестя если не нужно просто
# коментируем декоратор
