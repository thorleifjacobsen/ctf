from flask import Flask, request, render_template
import urllib.request

app = Flask(__name__)


def visit(url):
    return urllib.request.urlopen(url).read().decode('utf-8')


@app.route('/', methods=['GET', 'POST'])
def index():
    content = ''
    url = request.form.get('url')

    if request.method == 'POST':
        try:
            content = visit(url)
        except Exception as e:
            content = f"Error: {e}"
    return render_template('index.html', content=content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
