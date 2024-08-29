import random

def prepare_random_data(records_amount, item_list, max_amount, min_amount=1, company_order=False, companies=None):
    """
    Prepares a list of random order data based on the provided item list.
    
    Args:
        records_amount (int): The number of records to generate.
        item_list (list of tuples): The list of items to choose from, each item being a tuple.
        max_amount (int): The maximum quantity for each item in the order.
        min_amount (int, optional): The minimum quantity for each item. Default is 1.
        company_order (bool, optional): If True, associates orders with random companies. Default is False.
        companies (list of str, optional): The list of companies to choose from if company_order is True.

    Returns:
        list of tuples: A list of generated order data, optionally including company names.
    """
    prepared_data = []
    
    for _ in range(records_amount):
        # Select a random item from the item list
        item_number = random.randint(0, len(item_list) - 1)
        
        # Generate a random quantity within the specified range
        item_quantity = random.randint(min_amount, max_amount)
        
        # Create a new record by combining the item with its random quantity
        new_record = item_list[item_number][:1] + (item_quantity,) + item_list[item_number][1:]
        
        # Append the new record to the prepared data list
        prepared_data.append(new_record)
    
    # If company_order is True, add company names to the records
    if company_order:
        return add_company_name(prepared_data, companies)
    
    return prepared_data

def add_company_name(prepared_data, companies):
    """
    Adds a random company name to each order in the prepared data.
    
    Args:
        prepared_data (list of tuples): The list of order data to which company names will be added.
        companies (list of str): The list of companies to choose from.
    
    Returns:
        list of tuples: The updated list of order data with company names added.
    """
    company_orders = []
    
    for order in prepared_data:
        # Select a random company from the companies list
        company_number = random.randint(0, len(companies) - 1)
        
        # Append the selected company name to the order
        new_record = order + (companies[company_number],)
        
        # Add the new record to the list of company orders
        company_orders.append(new_record)
    
    return company_orders