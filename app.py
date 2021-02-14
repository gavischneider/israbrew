# Start venv: source venv/bin/activate
# Export app: export FLASK_APP=server/app

from israbrew import app

if __name__ == '__main__':
    print('APP MAIN')
    app.run(debug=True, use_reloader=False)
    #app.run(debug=True)

