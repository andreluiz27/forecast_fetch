from pydantic import BaseModel, Field


class CityWeather(BaseModel):
    """
    Represents the weather information for a city.

    Attributes:
        userdefined_id (str): Userdefined ID for the city weather.
        city_id (int): ID of the city.
        temperature (float): Temperature in Celsius.
        humidity (int): Humidity in percentage.
    """

    userdefined_id: str = Field(
        ...,
        title="Userdefined ID",
        description="Userdefined ID",
        example="e7b3b3b3-3b3b-3b3b-3b3b-3b3b3b3b3b3b",
    )
    city_id: int = Field(..., title="City ID", description="City ID", example=2643743)
    temperature: float = Field(
        ..., title="Temperature", description="Temperature in Celsius", example=12.5
    )
    humidity: int = Field(
        ..., title="Humidity", description="Humidity in percentage", example=50
    )


class CitiesForecastResponse(BaseModel):
    """
    Represents the response containing the forecast for multiple cities.
    """

    progress: float = Field(
        ..., title="Progress", description="Progress in percentage", example=50.0
    )
    city_weathers: list[CityWeather] = Field(
        ...,
        title="City Weathers",
        description="City Weathers",
        # example=[
        #     {
        #         "userdefined_id": "e7b3b3b3-3b3b-3b3b-3b3b-3b3b3b3b3b3b",
        #         "city_id": 2643743,
        #     }
        # ],
    )


class ProgressResponse(BaseModel):
    """
    Represents a progress response object.

    Attributes:
        progress (float): The progress in percentage.
        userdefined_id (str): The user-defined ID.
    """

    progress: float = Field(
        ..., title="Progress", description="Progress in percentage", example=50.0
    )
    userdefined_id: str = Field(
        ...,
        title="Userdefined ID",
        description="Userdefined ID",
        example="e7b3b3b3-3b3b-3b3b-3b3b-3b3b3b3b3b3b",
    )
