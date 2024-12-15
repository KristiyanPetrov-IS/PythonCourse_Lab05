import aiohttp
import asyncio
from defines import *


async def fetch_trending_data(session, media_type: str, time_window: str):
    url = f"{BASE_URL}/{media_type}/{time_window}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    async with session.get(url, headers=headers) as response:
        response.raise_for_status()
        data = await response.json()
        return data['results']

async def get_trending(media_type: str, time_window: str):
    async with aiohttp.ClientSession() as session:
        tasks = []
        
        if media_type == 'all' or media_type == 'movie':
            tasks.append(fetch_trending_data(session, 'movie', time_window))
        if media_type == 'all' or media_type == 'tv':
            tasks.append(fetch_trending_data(session, 'tv', time_window))
        
        trending_data = await asyncio.gather(*tasks)

        formatted_results = [
            {"title": item["title"] if "title" in item else item["name"], "rating": item["vote_average"]}
            for item in trending_data[0]
            ]
        
        if media_type == 'all':
            formatted_results_extra = [
            {"title": item["title"] if "title" in item else item["name"], "rating": item["vote_average"]}
            for item in trending_data[1]
            ]
            formatted_results.extend(formatted_results_extra)
        
        sorted_results = sorted(formatted_results, key=lambda x: x["rating"], reverse=True)
        
        return sorted_results
    
    