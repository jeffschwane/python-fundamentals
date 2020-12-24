'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''


def decorator_func(initial_func):
    def wrapper_func():
        return '<p> ' + initial_func() + ' </p>'
    return wrapper_func


@decorator_func
def html_text():
    return 'This is my html text'


print(html_text())
