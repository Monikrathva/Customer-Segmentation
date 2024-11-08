from faker import Faker
import random
import pandas as pd
from datetime import timedelta

# Initialize Faker
fake = Faker()

# Set a seed for reproducibility
Faker.seed(42)

# Generate synthetic data


def generate_synthetic_data(num_customers=100):
    data = []
    for _ in range(num_customers):
        customer_id = fake.unique.uuid4()
        order_id = fake.unique.ean13()  # Generating a random 13-digit Order ID
        customer_name = fake.name()
        order_date = fake.date_between(start_date='-3y', end_date='today')
        ship_date = order_date + timedelta(days=random.randint(1, 10))
        ship_mode = random.choice(
            ['Standard Class', 'Second Class', 'First Class', 'Same Day'])
        country = "United States"
        city = fake.city()
        state = fake.state()
        postal_code = fake.zipcode()
        region = random.choice(['West', 'East', 'South', 'Central'])
        category = random.choice(
            ['Furniture', 'Office Supplies', 'Technology'])
        sub_category = random.choice(
            ['Bookcases', 'Chairs', 'Tables', 'Phones', 'Binders'])
        product_name = fake.catch_phrase()
        sales = round(random.uniform(20, 2000), 2)
        quantity = random.randint(1, 10)
        discount = round(random.uniform(0, 0.5), 2)
        profit = round(sales * (1 - discount), 2) - random.uniform(5, 50)

        data.append([order_id, customer_id, customer_name, order_date, ship_date, ship_mode, city, state, postal_code,
                     region, category, sub_category, product_name, sales, quantity, discount, profit])

    # Create DataFrame
    df_synthetic = pd.DataFrame(data, columns=['Order ID', 'Customer ID', 'Customer Name', 'Order Date', 'Ship Date',
                                               'Ship Mode', 'City', 'State', 'Postal Code', 'Region', 'Category',
                                               'Sub-Category', 'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit'])
    return df_synthetic


# Generate 100 synthetic customers for testing
synthetic_data = generate_synthetic_data(1000)

# Save the synthetic data to a CSV file
csv_file_path = 'Furniture Customer Segmentation\synthetic_customer_data.csv'
synthetic_data.to_csv(csv_file_path, index=False)

print(f"Synthetic data saved to {csv_file_path}")
