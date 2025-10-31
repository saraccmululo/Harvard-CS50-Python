import sys
import requests
import json


API_KEY = "e7ab8734f3032fd11d5524daba9972525a793292195d70a85ba5ebe776d73962"


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin", headers=headers)
        # print(json.dumps(response.json(), indent=2)) #shows the JSON response content

        result = response.json()  # .json() converts response to Python dictionary
        price = float(result["data"]["priceUsd"])
        amount = price*n
        print(f"${amount:,.4f}")

    except requests.RequestException as e:
        print("Network error: ", e)


main()
