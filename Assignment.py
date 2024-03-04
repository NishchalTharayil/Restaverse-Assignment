import requests
import pandas as pd
import sys


def fetch_menu_data():
    # API endpoint for fetching menu data from Swiggy
    api_url = f"https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu=true&lat=18.56&lng=73.95&restaurantId=37968"

    # Headers to be sent with the HTTP request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'application/json',
        'Referer': 'https://www.swiggy.com/',
    }

    try:
        # Send HTTP GET request to the Swiggy API
        response = requests.get(api_url, headers=headers)

        # Check for any request errors
        response.raise_for_status()

        # Parse the JSON response
        menu_data = response.json()
        return menu_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Swiggy API: {e}")
        sys.exit(1)


def extract_menu_details(json_data):
    menu_details = []

    try:
        # Extracting 'cards' section from the JSON data
        cards = json_data.get('data', {}).get('cards', [])

        for card in cards:
            # Determine the type of card
            card_type = card.get('card', {}).get('card', {}).get('@type', '')

            # If the card represents a restaurant
            if card_type == 'type.googleapis.com/swiggy.presentation.food.v2.Restaurant':
                restaurant_info = card.get('card', {}).get('card', {}).get('info', {})
                restaurant_name = restaurant_info.get('name', '')
                category_title = restaurant_info.get('areaName', '')
                cost_for_two = restaurant_info.get('costForTwo', '')

                # Debug print
                print(f"Checking card for {restaurant_name}")

                # Check for the presence of 'itemCards' directly in the card
                if 'itemCards' in card.get('card', {}).get('card', {}):
                    item_cards = card['card']['card']['itemCards']

                    # Debug print
                    print(f"Number of item cards for {restaurant_name}: {len(item_cards)}")

                    for item_card in item_cards:
                        dish_info = item_card.get('card', {}).get('info', {})
                        dish_name = dish_info.get('name', '')
                        dish_price = dish_info.get('price', 0) / 100  # Convert to actual currency
                        dish_description = dish_info.get('description', 'No description available')

                        # Append extracted details to the menu_details list
                        menu_details.append({
                            'RestaurantName': restaurant_name,
                            'Category': category_title,
                            'DishName': dish_name,
                            'Price': dish_price,
                            'Description': dish_description,
                        })

            # If the card represents a grid widget with offers
            elif card_type == 'type.googleapis.com/swiggy.gandalf.widgets.v2.GridWidget':
                # Extracting offers
                offer_info = card.get('card', {}).get('card', {}).get('gridElements', {}).get('infoWithStyle', {})
                offers = offer_info.get('offers', [])

                for offer in offers:
                    header = offer.get('info', {}).get('header', '')
                    coupon_code = offer.get('info', {}).get('couponCode', '')
                    description = offer.get('info', {}).get('description', '')

                    # Append extracted offer details to the menu_details list
                    menu_details.append({
                        'OfferHeader': header,
                        'CouponCode': coupon_code,
                        'OfferDescription': description,
                    })

    except KeyError as e:
        print(f"Error extracting menu details: {e}")
        sys.exit(1)

    # Return the extracted menu details (or None if empty)
    return menu_details if menu_details else None


if __name__ == "__main__":
    # Fetch menu data from Swiggy API
    menu_data = fetch_menu_data()

    # Extract menu details
    extracted_menu_details = extract_menu_details(menu_data)

    # Display extracted menu details
    if extracted_menu_details:
        print("Extracted Menu Details:")
        for item in extracted_menu_details:
            print(item)
    else:
        print("No menu details extracted.")

