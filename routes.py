from config import app
from cont_functions import home, create_author, create_book

app.add_url_rule("/", view_func=home)

app.add_url_rule("/create_author", view_func=create_author, methods = ["POST"])

app.add_url_rule("/create_book", view_func=create_book, methods = ["POST"])