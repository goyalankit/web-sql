"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, request, render_template
from Webpage import Webpage
from flask_bootstrap import Bootstrap
from queryForm import QueryForm

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