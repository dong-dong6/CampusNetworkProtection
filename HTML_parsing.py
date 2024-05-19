from bs4 import BeautifulSoup
import re

def extract_js_variables_from_html(input_string, param_list):
    print(input_string)
    """
    Extracts the values of specified parameters from the input string.

    Parameters:
    - input_string: The string to search through.
    - param_list: A list of parameter names to search for.

    Returns:
    A dictionary with parameter names as keys and their corresponding values as values.
    """
    # Initialize an empty dictionary to store the results
    results = {}

    # Loop through each parameter in the list
    for param in param_list:
        # Create a regular expression pattern to match the parameter and extract its value
        # The pattern assumes that the parameter is followed by an '=' and then its value,
        # which is captured in the group (.*?); it stops capturing when a semicolon or whitespace is encountered.
        pattern = fr"{param}=['\"](.*?)['\"]"

        # Search for the pattern in the input string
        match = re.search(pattern, input_string)

        # If a match is found, add the parameter and its value to the results dictionary
        if match:
            results[param] = match.group(1)
    print(results)
    return results


