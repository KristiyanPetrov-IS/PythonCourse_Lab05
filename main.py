import sys
import asyncio
from api import get_trending
from output_handler import print_json, print_csv

async def handle_trending_request(media_type: str, time_window: str, output_format: str):
    trending_data = await get_trending(media_type, time_window)
    
    if output_format == "json":
        print_json(trending_data)
    elif output_format == "csv":
        print_csv(trending_data)

async def main():
    if len(sys.argv) != 4:
        print("Invalid number of arguments")
        sys.exit(1)
    
    media_type, time_window, output_format = sys.argv[1], sys.argv[2], sys.argv[3]
    
    if media_type not in ["tv", "movie", "all"]:
        print("Invalid media type")
        sys.exit(1)
    
    if time_window not in ["day", "week"]:
        print("Invalid time window")
        sys.exit(1)
    
    if output_format not in ["csv", "json"]:
        print("Invalid output format")
        sys.exit(1)

    await handle_trending_request(media_type, time_window, output_format)


if __name__ == "__main__":
    asyncio.run(main())
