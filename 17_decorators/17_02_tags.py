'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''


def decorator_arg(tag):
    def decorator_func(initial_func):
        def wrapper_func():
            return f'<{tag}> {initial_func()} </{tag}>'
        return wrapper_func
    return decorator_func


@decorator_arg('h')
def html_text():
    return 'This is my html text'


print(html_text())
