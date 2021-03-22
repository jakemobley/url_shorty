import flask
from flask import render_template, request, redirect
from send_and_receive_data.send_and_receive_data import send_and_receive_data
app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    """ Give and receive information to/from User """
    if not request.args:
        return render_template('submit_form.html')
    if request.args:
        short_url_text, long_url_text = request.args.get('short_url_text'), request.args.get('long_url_text')
        return render_template('submit_form.html', short_url_text=short_url_text, long_url_text=long_url_text)


@app.route('/shorten/')
def shorten():
    """ Retrieve a shortened link for a long-form (destination) link and create one if not already present """
    long_url_text = request.args.get('long_url')
    long_url_text = long_url_text.strip()
    short_url_res = send_and_receive_data(request_type="get_short", url=long_url_text)
    short_url = short_url_res.in_url()
    return redirect(f"/?short_url_text={short_url}&long_url_text={long_url_text}")


@app.route('/lengthen/')
def lengthen():
    """ Retrieve a long-form (destination) link for a previously shortened link """
    short_url_text = request.args.get('short_url')
    short_url_text = short_url_text.strip()
    long_url_res = send_and_receive_data(request_type="get_long", url=short_url_text)
    long_url = long_url_res.in_url()
    if not long_url:
        long_url = "No long-form URL found for that shorty. Are you sure you shortened it before?"
    return redirect(f"/?short_url_text={short_url_text}&long_url_text={long_url}")


if __name__ == "__main__":
    app.run(debug=True)
