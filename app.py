# Start venv: source venv/bin/activate
# Export app: export FLASK_APP=server/app

#from israbrew import create_app

#app = create_app()
#app.app_context().push()

from israbrew import app

if __name__ == '__main__':
    print('APP MAIN')
    app.run(debug=True)

