import os
import django
import uuid
from decimal import Decimal

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mutts.settings")
django.setup()

from api.products.models import Category, Product
from api.customers.models import Customer, Address
from api.orders.models import Order

def populate_categories():
    categories = ["Chaveirinho", "Caderno", "Caneca", "Camisa"]
    for cat in categories:
        Category.objects.get_or_create(name=cat)

def populate_products():
    products = [
        {"code": "LMPI0001", "desc_short": "Capa para notas adesivas gato", "category": "Chaveirinho", "price": 12.23, "stock": 10, "weight": 0.5, "height": 10.0, "width": 8.0, "length": 2.0, "image": "product1.jpg"},
        {"code": "LMPI0002", "desc_short": "Caderno Mutts", "category": "Caderno", "price": 25.50, "stock": 5, "weight": 1.0, "height": 20.0, "width": 15.0, "length": 2.0, "image": "product2.jpg"},
        {"code": "LMPI0003", "desc_short": "Caneca Personalizada", "category": "Caneca", "price": 35.00, "stock": 8, "weight": 0.8, "height": 12.0, "width": 10.0, "length": 10.0, "image": "product3.jpg"},
    ]

    for item in products:
        category = Category.objects.get(name=item["category"])
        Product.objects.get_or_create(
            product_code=item["code"],
            product_description_short=item["desc_short"],
            product_category=category,
            product_unit_price=item["price"],
            product_stock=item["stock"],
            product_weight=item["weight"],
            product_height=item["height"],
            product_width=item["width"],
            product_length=item["length"],
            product_image_url=f"products/{item['image']}"
        )

def populate_customers():
    customers = [
        {"cpf": "12345678901", "name": "Antonio Silva", "phone": "11999999999", "email": "antonio@example.com"},
        {"cpf": "98765432100", "name": "Maria Souza", "phone": "21988888888", "email": "maria@example.com"},
    ]

    for cust in customers:
        customer, created = Customer.objects.get_or_create(
            customer_cpf=cust["cpf"],
            customer_name=cust["name"],
            customer_phone=cust["phone"],
            customer_email=cust["email"]
        )

        Address.objects.get_or_create(
            customer=customer,
            zip_code="01001000",
            street="Rua Exemplo",
            neighborhood="Bairro Exemplo",
            city="São Paulo",
            state="SP",
            house_number="100"
        )

def populate_orders():
    customer = Customer.objects.get(customer_cpf="12345678901")
    product = Product.objects.get(product_code="LMPI0001")

    Order.objects.create(
        order_ID=uuid.uuid4(),
        order_payment_ID=uuid.uuid4(),
        order_status="approved",
        order_cpf=customer,
        order_product_code=product,
        order_product_unit_price=product.product_unit_price,
        order_quantity=2,
        order_freight_cost=Decimal("10.00"),
        order_freight_service="SEDEX",
        order_zip_code="01001000",
        order_street="Rua Exemplo",
        order_neighborhood="Bairro Exemplo",
        order_city="São Paulo",
        order_state="SP",
        order_house_number="100",
        order_phone=customer.customer_phone
    )

if __name__ == "__main__":
    print("📌 Populating Database...")
    populate_categories()
    populate_products()
    populate_customers()
    populate_orders()
    print("✅ Database populated successfully!")
