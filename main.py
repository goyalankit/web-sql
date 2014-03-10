"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, request, render_template
from Webpage import Webpage
from flask_bootstrap import Bootstrap
from queryForm import QueryForm
from SqlParser import SQLParser

app = Flask(__name__)
Bootstrap(app)



#
# Home page.
#


@app.route('/')
def home():
    form = QueryForm()
    return render_template('home.html', form=form)



#
# url handler. Fetch the page and store it in redis.
#

@app.route('/url', methods=['POST'])
def url_handler():
    if request.form['url'] is not None:
        w = Webpage(request.form['url'])
        w.store_content(w.get_content())
        return w.retreive_content()
        #return render_template('url_result.html')
    else:
        return "url parameter not given."





@app.route('/query')
def query():
    if request.args.get('query') is not None:

        sql_parser = SQLParser(request.args.get('query'))
        stmt = sql_parser.parse()

        " Only valid query is SELECT query "
        if stmt is None:
            return "Invalid Query"

        table_name = sql_parser.understand()
        if table_name is not None:
            Webpage.get_star(table_name)

        return "cool"
    else:
        return "query not present"



##
##
##
## Error handling dumb methods
##
##
##

#
# Error Handler. Custom 404 page
#


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500


if __name__ == "__main__":
    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = \
        '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
    app.run()