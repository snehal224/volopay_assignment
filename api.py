from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset
dataset_path = "data.csv"  # Update with the actual path to the dataset
df = pd.read_csv(dataset_path)

# API 1: Total items sold in Marketing for last in Q3 of the year
@app.route('/api/total_items', methods=['GET'])
def total_items():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    department = request.args.get('department')

    # Filter the dataset based on the parameters
    filtered_df = df[
        (df['date'] >= start_date) &
        (df['date'] <= end_date) &
        (df['department'] == department)
    ]

    total_items_sold = filtered_df['quantity'].sum()

    return jsonify(total_items_sold)


# API 2: Nth most sold item in terms of quantity sold in Q4 or total price in Q2
@app.route('/api/nth_most_total_item', methods=['GET'])
def nth_most_total_item():
    item_by = request.args.get('item_by')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    n = int(request.args.get('n'))

    if item_by == 'quantity':
        # Filter the dataset for Q4
        filtered_df = df[
            (df['date'] >= start_date) &
            (df['date'] <= end_date) &
            (df['date'].str.endswith('Q4'))
        ]

        # Get the nth most sold item by quantity
        nth_item = filtered_df.groupby('item')['quantity'].sum().nlargest(n).index[n-1]

    elif item_by == 'price':
        # Filter the dataset for Q2
        filtered_df = df[
            (df['date'] >= start_date) &
            (df['date'] <= end_date) &
            (df['date'].str.endswith('Q2'))
        ]

        # Get the nth most sold item by total price
        filtered_df['total_price'] = filtered_df['quantity'] * filtered_df['price']
        nth_item = filtered_df.groupby('item')['total_price'].sum().nlargest(n).index[n-1]

    return jsonify(nth_item)


# API 3: Percentage of sold items (seats) department-wise
@app.route('/api/percentage_of_department_wise_sold_items', methods=['GET'])
def percentage_of_department_wise_sold_items():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Filter the dataset based on the parameters
    filtered_df = df[
        (df['date'] >= start_date) &
        (df['date'] <= end_date)
    ]

    department_wise_sold_items = filtered_df.groupby('department')['quantity'].sum()
    total_sold_items = department_wise_sold_items.sum()

    percentage_sold_items = department_wise_sold_items / total_sold_items * 100

    return jsonify(percentage_sold_items.to_dict())


# API 4: Monthly sales for any product
@app.route('/api/monthly_sales', methods=['GET'])
def monthly_sales():
    product = request.args.get('product')
    year = int(request.args.get('year'))

    # Filter the dataset based on the parameters
    filtered_df = df[
        (df['item'] == product) &
        (df['date'].str.startswith(str(year)))
    ]

   
