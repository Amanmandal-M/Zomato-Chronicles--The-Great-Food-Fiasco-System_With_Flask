from flask import Blueprint, render_template, request

# Import the required controllers
from controllers.zomato_controllers import (
    display_menu, take_order, add_items, update_items, delete_items, all_orders, review_orders
)

# Create a Blueprint for the Zomato routes
zomato_router = Blueprint('zomato', __name__)

# Routes with comments

# Route: Display Menu
# Method: GET
# Description: Displays the menu
zomato_router.route('/menu', methods=['GET'])(display_menu)

# Route: All Orders
# Method: GET
# Description: Get all orders
zomato_router.route('/orders', methods=['GET'])(all_orders)

# Route: Review Orders
# Method: GET
# Description: Review all orders
zomato_router.route('/review-orders', methods=['GET'])(review_orders)

# Route: Take Order
# Method: POST
# Description: Takes an order
zomato_router.route('/take-order', methods=['POST'])(take_order)

# Route: Add Items
# Method: POST
# Description: Add items to the menu
zomato_router.route('/add-items', methods=['POST'])(add_items)

# Route: Update Items
# Method: PATCH
# Description: Update the availability and quantity of a dish
zomato_router.route('/update-items/<dish_id>', methods=['PATCH'])(update_items)

# Route: Delete Items
# Method: DELETE
# Description: Delete a dish from the menu
zomato_router.route('/delete-items/<dish_id>', methods=['DELETE'])(delete_items)

