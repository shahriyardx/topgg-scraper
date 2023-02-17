from urllib.parse import unquote

import aiohttp
from bs4 import BeautifulSoup


async def scrape_reviews(bot_id: int):
    data: BeautifulSoup = None

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://top.gg/bot/{bot_id}") as resp:
            data = BeautifulSoup(await resp.text(), "html.parser")

    if not data:
        return []

    reviews = data.find_all("article", class_="css-141r8xx")
    all_reviews = []

    for review in reviews:
        review_data = {}
        images = review.find_all("img")

        for img in images:
            if "images.discordapp.net" in img["src"]:
                link = img["src"].split("url=")[-1].split("&")[0]
                review_data["image"] = unquote(link)
                break
        else:
            review_data["image"] = "https://cdn.discordapp.com/embed/avatars/0.png"

        full_review = review.find("div", recursive=False)
        header_data = full_review.find("div", class_="chakra-stack css-8h2221")
        footer_data = full_review.find("div", class_="css-ury6s2").find("p")
        name, time = header_data.getText().split("•")
        stars = header_data.find("div", {"data-stars": True})
        content = footer_data.getText()

        review_data["name"] = name
        review_data["time"] = time
        review_data["stars"] = stars["data-stars"]
        review_data["content"] = content

        all_reviews.append(review_data)

    return all_reviews
