# OShop: Online Shopping Platform

OShop is a comprehensive online shopping platform developed using Django. It facilitates users to explore a wide range of products, manage their shopping carts, and securely complete their purchases.

---

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Features

OShop offers a variety of features to enhance the online shopping experience:

- **User Authentication and Authorization**:
  - User registration with secure authentication mechanisms.
  - User login/logout functionality.
  - Authorization controls to manage user access levels.

- **Product Management**:
  - Browse products across different categories.
  - View detailed product descriptions, including images, prices, and specifications.
  - Search functionality to quickly find desired products.

- **Shopping Cart Management**:
  - Add products to the shopping cart.
  - Adjust product quantities or remove items from the cart.
  - Save items in the cart for future sessions.

- **Checkout and Payment Processing**:
  - Seamless checkout process with integrated payment gateways.
  - Support for various payment methods, including credit/debit cards, PayPal, and more.
  - Secure handling of sensitive payment information.

- **Order Tracking and Management**:
  - View order history and track the status of current orders.
  - Manage shipping addresses and payment preferences.
  - Receive email notifications for order confirmations and updates.

- **Admin Dashboard**:
  - Admin interface for managing products, orders, and user accounts.
  - Role-based access control for administrators to perform specific actions.

---

## Screenshots

Here are some screenshots showcasing the key functionalities of OShop:

### Home Page
![Home Page](https://raw.githubusercontent.com/RefatJamil/Django-Online-Shopping-Platform/main/demo/Screenshot%20from%202023-04-27%2009-29-26.png)

### Add to Cart
![Add to Cart](https://raw.githubusercontent.com/refat-jamil/Django-Online-Shopping-Platform/main/demo/add_to_cart.gif)

### PayPal Payment
![Order Placed](https://raw.githubusercontent.com/refat-jamil/Django-Online-Shopping-Platform/main/demo/payment.gif)

---

## Installation

Follow these instructions to set up OShop on your local machine:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/refatjamil/Django-Online-Shopping-Platform.git
    cd Django-Online-Shopping-Platform
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    sudo apt update
    sudo apt install python3 python3-venv
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    cd OShop
    ```

4. **Run Migrations and Start the Server**:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

5. **Access the Application**:
    - Open a web browser and navigate to `http://127.0.0.1:8000/` to access the OShop application.

---
