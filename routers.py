from cities import cities_id
from database import forecast_collection
import asyncio
from schemas import ProgressResponse, CitiesForecastResponse
from fastapi import APIRouter
from helpers import city_forecast
import httpx
from settings import DELAY_TIME, MAX_QTY_CITY
router = APIRouter()
requests_client = httpx.AsyncClient()


@router.get("/")
async def root():
    """
    Returns a JSON response with a message "Hello World".
    """
    return {"message": "Hello World"}


@router.post("/forecast")
async def get_forecast(user_id: str):
    """
    Get forecast for a user.

    Args:
        user_id (str): The ID of the user.

    Returns:
        dict: A dictionary containing the user ID or an error message if the user already exists.
    """

    # check if the user exist in mongo database otherwise error
    user = await forecast_collection.find_one({"userdefined_id": user_id})
    if user:
        return {"error": "User already exists"}

    # delay five seconds
    delay_set = float(DELAY_TIME)
    delay = delay_set
    for city_id in cities_id:
        # asynchronously call city_forecast
        delay += delay_set
        try:
            asyncio.create_task(
                city_forecast(user_id, city_id, request_client=requests_client, delay=delay)
            )
        except Exception as e:
            # write log in a file
            with open("error.log", "a") as f:
                f.write(f"{str(e)}\n")

    return {"user_id": user_id}


@router.get("/check_process")
async def check_process(user_id: str):
    """
    Check the progress of forecast generation for a given user.

    Args:
        user_id (str): The user-defined ID of the user.

    Returns:
        dict: A dictionary containing the progress response.

    Raises:
        None

    Example:
        >>> check_process("12345")
        {'userdefined_id': '12345', 'progress': 50.0}
    """

    # check if user does not exist in mongo database
    user = await forecast_collection.find_one({"userdefined_id": user_id})
    if not user:
        return {"error": "User does not exist"}
    
    # counting how many forecast are done
    forecast = await forecast_collection.find({"userdefined_id": user_id}).to_list(
        length=MAX_QTY_CITY
    )
    progress = round(100 * (len(forecast) / len(cities_id)), 2)

    response = ProgressResponse(userdefined_id=user_id, progress=progress)

    return response


@router.post("/check_process")
async def check_process(user_id: str):
    """
    Check the process for a given user ID.

    Args:
        user_id (str): The user ID to check the process for.

    Returns:
        dict: A dictionary containing the progress of the process and the forecast for each city.

    Raises:
        dict: If the user does not exist in the database, an error message is returned.
    """
    
    # check if user does not exist in mongo database
    user = await forecast_collection.find_one({"userdefined_id": user_id})
    if not user:
        return {"error": "User does not exist"}
    
    forecast = await forecast_collection.find({"userdefined_id": user_id}).to_list(
        length=MAX_QTY_CITY
    )

    response_as_list = []
    for f in forecast:
        f.pop("_id")
        response_as_list.append(f)

    progress = round(100 * (len(response_as_list) / len(cities_id)), 2)
    return CitiesForecastResponse(progress=progress, city_weathers=response_as_list)
