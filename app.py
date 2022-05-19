from flask import Flask
from youtubeComments import youtubeComments
from redditComments import redditComments
app = Flask(__name__)

app.register_blueprint(youtubeComments, url_prefix="/ytct")
app.register_blueprint(redditComments, url_prefix="/ric")

if __name__ == '__main__':
    app.run(debug = True)

