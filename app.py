# Start venv: source venv/bin/activate
# Export app: export FLASK_APP=server/app

from israbrew import app
    
if __name__ == '__main__':
    app.run(debug=True)