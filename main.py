from quart import Quart
from quart_cors import cors

from utils.scraper import scrape_reviews

app = Quart(__name__)
app = cors(app, allow_origin="*")


@app.get("/reviews/<string:bot_id>")
async def reviews(bot_id):
    return await scrape_reviews(bot_id)


if __name__ == "__main__":
    app.run(port=5000)
