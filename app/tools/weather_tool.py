import httpx

from langchain_core.tools import tool


@tool
async def get_weather(
    city: str,
) -> dict:
    """
    Get the current weather for a city.

    Use this tool when the user asks about:
    - current weather
    - temperature
    - rain
    - weather conditions
    """

    try:

        async with httpx.AsyncClient(
            timeout=10
        ) as client:

            geo_response = await client.get(
                "https://geocoding-api.open-meteo.com/v1/search",
                params={
                    "name": city,
                    "count": 1,
                    "language": "en",
                    "format": "json",
                },
            )

            geo_response.raise_for_status()

            geo_data = geo_response.json()

            results = geo_data.get(
                "results",
                [],
            )

            if not results:

                return {
                    "error": f"City '{city}' was not found."
                }

            location = results[0]

            latitude = location["latitude"]
            longitude = location["longitude"]

            weather_response = await client.get(
                "https://api.open-meteo.com/v1/forecast",
                params={
                    "latitude": latitude,
                    "longitude": longitude,
                    "current": (
                        "temperature_2m,"
                        "relative_humidity_2m,"
                        "precipitation,"
                        "weather_code"
                    ),
                },
            )

            weather_response.raise_for_status()

            weather = weather_response.json()

            return {
                "city": city,
                "latitude": latitude,
                "longitude": longitude,
                "current": weather.get(
                    "current",
                    {},
                ),
            }

    except httpx.HTTPError:

        return {
            "error": "Weather service unavailable."
        }