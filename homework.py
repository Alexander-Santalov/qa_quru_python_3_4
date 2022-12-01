def print_name_func_and_args(name, *args):
    case_camel = name[0] + name.title().replace("_", "")[1:]
    print(f"\nИмя функции: {case_camel}\nЗначения аргументов: {', '.join([i for i in args])}") if len(args) > 1 \
        else print(f"\nИмя функции: {case_camel}\nЗначение аргумента: {''.join([i for i in args])}")


def open_browser(browser_name):
    print_name_func_and_args(open_browser.__name__, browser_name)


def go_to_companyname_homepage(page_url):
    print_name_func_and_args(go_to_companyname_homepage.__name__, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_name_func_and_args(find_registration_button_on_login_page.__name__, page_url, button_text)


open_browser("Firefox")
go_to_companyname_homepage("https://yandex.ru")
find_registration_button_on_login_page("https://yandex.ru", "Найти")
