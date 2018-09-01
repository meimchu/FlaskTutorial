from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Mei's World"
