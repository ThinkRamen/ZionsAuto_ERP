import requests

BASE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles"


def get_vin_decode(vin):
    def get_val_by_var(filtered_data, var_name):
        """
        Retrieve the value associated with a variable name from filtered data.

        Args:
            filtered_data (list): List of dictionaries containing filtered data.
            variable_name (str): Name of the variable to retrieve the value for.

        Returns:
            str or None: Value associated with the variable, or None if not found.
        """

        var_info = next(
            (item for item in filtered_data if item["Variable"] == var_name), None
        )
        return var_info["Value"] if var_info else None

    api_url = f"{BASE_URL}/DecodeVin/{vin}?format=json"
    response = requests.get(api_url)

    try:
        response.raise_for_status()
        data = response.json().get("Results", [])

        # Filter out null values from the response
        filtered_data = [
            {k: v for k, v in item.items() if v is not None} for item in data
        ]

        # Retrieve decoded information
        model_year = get_val_by_var(filtered_data, "Model Year")
        make = get_val_by_var(filtered_data, "Make")
        series = get_val_by_var(filtered_data, "Series")
        model = get_val_by_var(filtered_data, "Model")
        trim = get_val_by_var(filtered_data, "Trim")
        body_style = get_val_by_var(filtered_data, "Body Class")
        doors = get_val_by_var(filtered_data, "Doors")
        fuel_type_primary = get_val_by_var(filtered_data, "Fuel Type - Primary")
        cylinder_count = get_val_by_var(filtered_data, "Engine Number of Cylinders")
        engine_size = get_val_by_var(filtered_data, "Displacement (L)")

        return {
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


# Call the function to retrieve decoded information for a VIN
decoded_info = get_vin_decode("WVWHV71K59W063568")
print("Filtered Decoded Information:", decoded_info)

# Call the function to retrieve models for a make
models_for_make = get_models_for_make("Honda")
print("Models for Honda:", models_for_make)
