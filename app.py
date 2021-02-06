# Start venv: source venv/bin/activate
# Export app: export FLASK_APP=server/app

from israbrew import app
from israbrew.routes import scrape_async
import asyncio
import threading
    
async def asyncc():
    await scrape_async()


if __name__ == '__main__':
    #scrape_async()
    x = threading.Thread(target=asyncc, daemon=True)
    x.start()
    app.run(debug=True)