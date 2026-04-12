from flask import Flask, request
import os

app = Flask(__name__)

# Log PORT status on startup.
print("PORT:", os.environ.get("PORT"))


@app.get("/getcustomers", strict_slashes=False)
def get_customers():
    customers = get_customers_data()
    return customers


def get_customers_data():
    customers = [
        {'customer_id': 1, 'name': 'Emily Carter', 'address': '742 Evergreen Terrace', 'city': 'Springfield', 'state': 'Illinois', 'zipcode': '62701', 'country': 'United States'},
        {'customer_id': 2, 'name': 'Marcus Johnson', 'address': '891 Lakeview Blvd Apt. 12', 'city': 'Lakewood', 'state': 'Colorado', 'zipcode': '80215', 'country': 'United States'},
        {'customer_id': 3, 'name': 'Sophia Rivera', 'address': '334 Maple Grove Lane', 'city': 'Sunnyvale', 'state': 'California', 'zipcode': '94086', 'country': 'United States'},
        {'customer_id': 4, 'name': 'Nathan Brooks', 'address': '55 Pinecrest Drive Suite 300', 'city': 'Asheville', 'state': 'North Carolina', 'zipcode': '28801', 'country': 'United States'},
        {'customer_id': 5, 'name': 'Olivia Bennett', 'address': '1203 Sunset Boulevard Apt. 7', 'city': 'Portland', 'state': 'Oregon', 'zipcode': '97201', 'country': 'United States'},
        {'customer_id': 6, 'name': 'James Thornton', 'address': '678 Ridgewood Avenue', 'city': 'Burlington', 'state': 'Vermont', 'zipcode': '05401', 'country': 'United States'},
        {'customer_id': 7, 'name': 'Aisha Montgomery', 'address': '2250 Oak Street Suite 110', 'city': 'Atlanta', 'state': 'Georgia', 'zipcode': '30301', 'country': 'United States'},
        {'customer_id': 8, 'name': 'Tyler Nguyen', 'address': '99 Birchwood Court Apt. 4B', 'city': 'Austin', 'state': 'Texas', 'zipcode': '73301', 'country': 'United States'},
        {'customer_id': 9, 'name': 'Rachel Simmons', 'address': '4410 Willow Creek Road', 'city': 'Boise', 'state': 'Idaho', 'zipcode': '83701', 'country': 'United States'},
        {'customer_id': 10, 'name': 'Derek Patel', 'address': '317 Elmwood Drive Suite 22', 'city': 'Phoenix', 'state': 'Arizona', 'zipcode': '85001', 'country': 'United States'},
    ]
    return customers
