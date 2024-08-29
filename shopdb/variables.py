detail_orders_schema = '''
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    category TEXT
'''

company_orders_schema = '''
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    category TEXT,
    company_name TEXT
'''

companies = ('ABC', 'Nemo', "Melo Market", 'Velo', 'Mix Market')

details_insert_schema = '(product_name, quantity, price, category)'

company_insert_schema = '(product_name, quantity, price, category, company_name)'

item_list = [
    ('Laptop', 1500.00, 'Electronics'),
    ('Smartphone', 600.00, 'Electronics'),
    ('Headphones', 150.00, 'Electronics'),
    ('Keyboard', 70.00, 'Electronics'),
    ('Mouse', 25.00, 'Electronics'),
    ('Monitor', 300.00, 'Electronics'),
    ('Printer', 120.00, 'Electronics'),
    ('Tablet', 250.00, 'Electronics'),
    ('Webcam', 45.00, 'Electronics'),
    ('USB Drive', 15.00, 'Electronics'),
    ('Apples', 0.50, 'Groceries'),
    ('Milk', 1.20, 'Groceries'),
    ('Bread', 1.00, 'Groceries'),
    ('Butter', 1.50, 'Groceries'),
    ('Cheese', 2.00, 'Groceries'),
    ('Chicken', 5.00, 'Groceries'),
    ('Beef', 10.00, 'Groceries'),
    ('Orange Juice', 3.00, 'Groceries'),
    ('Bananas', 0.30, 'Groceries'),
    ('Tomatoes', 0.80, 'Groceries'),
    ('Notebook', 3.00, 'Stationery'),
    ('Pen', 1.00, 'Stationery'),
    ('Pencil', 0.50, 'Stationery'),
    ('Eraser', 0.20, 'Stationery'),
    ('Marker', 2.00, 'Stationery'),
    ('Highlighter', 1.50, 'Stationery'),
    ('Stapler', 4.00, 'Stationery'),
    ('Scissors', 3.50, 'Stationery'),
    ('Glue', 2.00, 'Stationery'),
    ('Backpack', 20.00, 'Stationery')
]