from ShopDB import ShopDB
from variables import detail_orders_schema, details_insert_schema, item_list, companies, company_insert_schema, company_orders_schema
from utils import prepare_random_data
from collections import Counter

# Define the number of orders to generate
DETAIL_ORDERS_AMOUNT = 500
BUNCH_ORDERS_AMOUNT = 40

# Generate random data for detailed orders
detail_data_to_insert = prepare_random_data(DETAIL_ORDERS_AMOUNT, item_list, 3)

# Generate random data for company orders (wholesale)
company_data_to_insert = prepare_random_data(BUNCH_ORDERS_AMOUNT, item_list, 100, 20, True, companies)

# Create database and save new detailed orders data
detail_database = ShopDB('shopdb')
detail_database.create_model('detail_orders', detail_orders_schema)
detail_database.insert_data('detail_orders', details_insert_schema, detail_data_to_insert)
detail_data = detail_database.fetch_data('detail_orders')
detail_database.close()

# Create database and save new company orders data
company_db = ShopDB('shopdb')
company_db.create_model('company_orders', company_orders_schema)
company_db.insert_data('company_orders', company_insert_schema, company_data_to_insert)
company_data = company_db.fetch_data('company_orders')
company_db.close()

# Count the quantity of products ordered by category in detailed orders
counter_detail_orders = Counter()
for order in detail_data:
    category = order[1]  # Assuming category is at the second position (index 1)
    quantity = order[2]  # Assuming quantity is at the third position (index 2)
    counter_detail_orders[category] += quantity

# Count the quantity of products ordered by category in company orders (wholesale)
counter_company_orders = Counter()
for order in company_data:
    category = order[1]
    quantity = order[2]
    counter_company_orders[category] += quantity

# Sum the results from both data sources
total_counter = counter_detail_orders + counter_company_orders

# Display the results
print("Top 3 categories in detail orders:", counter_detail_orders.most_common(3))
print("Top 3 categories in company orders:", counter_company_orders.most_common(3))
print("Top 3 categories overall:", total_counter.most_common(3))