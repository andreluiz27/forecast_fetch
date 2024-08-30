import asyncio
from database import forecast_collection
from settings import API_KEY


async def city_forecast(userdefined_id, city_id: int, request_client, delay: float = 0.1):
    """
    Fetches the weather forecast for a given city and stores it in the database.

    Args:
        userdefined_id (str): The user-defined ID for the forecast.
        city_id (int): The ID of the city for which to fetch the forecast.
        request_client: The HTTP client used to make the API request.
        delay (float, optional): The delay in seconds before making the API request. Defaults to 0.1.

    Returns:
        None
    """
    await asyncio.sleep(delay)
    response = await request_client.get(
        f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}"
    )
    data = response.json()
    f = await forecast_collection.insert_one(
        {
            "userdefined_id": userdefined_id,
            "city_id": city_id,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
        }
    )
