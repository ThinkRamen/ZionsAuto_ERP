import requests
import asyncio

BASE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles"


def get_vin_decode(vin):
    def get_val_by_var(data, var_name):
        """
        Retrieve the value associated with a variable name from filtered data.

        Args:
            data (list): List of dictionaries containing filtered data.
            variable_name (str): Name of the variable to retrieve the value for.

        Returns:
            str or None: Value associated with the variable, or None if not found.
        """

        var_info = next((item for item in data if item["Variable"] == var_name), None)
        return var_info["Value"] if var_info else None

    api_url = f"{BASE_URL}/DecodeVin/{vin}?format=json"
    response = requests.get(api_url)

    try:
        response.raise_for_status()
        data = response.json().get("Results", [])
        print(data)

        # Retrieve decoded information
        model_year = get_val_by_var(data, "Model Year")
        make = get_val_by_var(data, "Make")
        series = get_val_by_var(data, "Series")
        model = get_val_by_var(data, "Model")
        trim = get_val_by_var(data, "Trim")
        body_style = get_val_by_var(data, "Body Class")
        doors = get_val_by_var(data, "Doors")
        fuel_type_primary = get_val_by_var(data, "Fuel Type - Primary")
        cylinder_count = get_val_by_var(data, "Engine Number of Cylinders")
        engine_size = get_val_by_var(data, "Displacement (L)")

        return {
            "Vin": vin,
            "Model Year": model_year,
            "Make": make,
            "Series": series,
            "Model": model,
            "Trim": trim,
            "Body Style": body_style,
            "Doors": doors,
            "Fuel Type - Primary": fuel_type_primary,
            "Engine Number of Cylinders": cylinder_count,
            "Displacement (L)": engine_size,
        }

    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred:", http_err)
    except ValueError as val_err:
        print("Value error occurred while decoding JSON:", val_err)
    except Exception as err:
        print("An error occurred:", err)
    return {}


def get_models_for_make(make):
    api_url = f"{BASE_URL}/GetModelsForMake/{make}?format=json"
    response = requests.get(api_url)
    data = response.json().get("Results", [])
    # Extract model names from the data
    model_names = [item["Model_Name"] for item in data]

    return model_names
