
Script: Swiggy Menu Data Extractor
Instructions to Run the Script:

1. Terminal

    cd Restaverse

2. Install Dependencies:

    pip install -r requirements.txt

3. Run the Script:

    python Assignment.py

Script Functionality:
The script fetches menu data from the Swiggy API, extracts essential details,
and structures the information into a readable format. Key functionalities include:

a)Fetching data from Swiggy API endpoint.
b)Extracting restaurant details: name, category, and cost for two.
c)Extracting dish details: name, price, and description.
d)Extracting offers: header, coupon code, and description.
e)Displaying the extracted details on the console.

Setup Steps (if applicable):
1)No environment variables or API keys are required for this script.
2)Ensure internet connectivity for fetching data from the Swiggy API.
3)The script uses Python 3. Make sure it is installed on your system.

Feel free to explore the code and modify it according to your needs. For any issues or improvements, please contact nishchaltharayil2001@gmail.com


Output:

Checking card for Burger King
Extracted Menu Details:
{'OfferHeader': '60% OFF UPTO ₹120', 'CouponCode': 'USE STEALDEAL', 'OfferDescription': 'ON SELECT ITEMS'}
{'OfferHeader': '50% OFF UPTO ₹100', 'CouponCode': 'USE SWIGGY50', 'OfferDescription': 'ABOVE ₹149'}
{'OfferHeader': 'Free Medium Fries', 'CouponCode': 'NO CODE REQUIRED', 'OfferDescription': 'ABOVE ₹549'}
{'OfferHeader': 'FLAT ₹50 OFF', 'CouponCode': 'NO CODE REQUIRED', 'OfferDescription': 'ABOVE ₹500'}
{'OfferHeader': '20% OFF UPTO ₹125', 'CouponCode': 'USE KOTAK125', 'OfferDescription': 'ABOVE ₹500'}

Process finished with exit code 0
