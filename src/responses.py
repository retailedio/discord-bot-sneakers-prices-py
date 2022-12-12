import os
import json
import httpx

from src import log

from typing import Dict, Any
from dotenv import load_dotenv

logger = log.setup_logger()

load_dotenv()


async def handle_response(sku, size_us) -> str:
    response = httpx.get(
        url="https://app.retailed.io/api/sneakers/prices",
        params={
            "product_sku": sku,
            "size_us": size_us
        },
        headers={
            "x-api-key": os.getenv('API')
        }
    )

    logger.info(f"API Status Response: '{response.status_code}'")

    p = json.loads(response.text)['data']

    message = f"**{p[0]['product']['name']}** {p[0]['sizeUs']}us - {p[0]['sizeEu']}eu ({p[0]['product']['sku']}) \n\n"

    for i in p:
        platform = i['platform']['name'].capitalize()
        if platform == "Stockx":
            platform = "StockX"
        if i['payoutUsd'] is not None and platform not in message:
            message += f"${i['payoutUsd']} at {platform} \n"

    return message
