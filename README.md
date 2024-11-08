# Payme One-Time Payment Implementation (Однаразовый платеж)

[Support Group - Telegram](https://t.me/+bYouuOlqt1c3NmYy)  
<!-- [YouTube - Watch Video](https://youtu.be/r2RO3kJVP7g)   -->
This MVP project helps to implement [payme-pkg](https://github.com/PayTechUz/payme-pkg).

<!-- [![Watch Video](https://i.postimg.cc/5NRRSHXp/homemuhammadali-Downloads-Telegram-Desktop-Closer-Li-QWYD-No-Copyright-Music-Audio-Library-Music-m4a.gif)](https://youtu.be/r2RO3kJVP7g) -->

### API Endpoints

Pay link is a simple interface that provides pay-link functionality.

- `/order/create/` POST: Get a pay link for each order.

### Merchant Endpoint

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/PayTechUz/shop-backend.git
   ```
2. Create a virtual environment and activate it:
   ```sh
   pip3 install virtualenv
   virtualenv venv
   ```
  - For Windows:
    ```sh
    venv\Scripts\activate
    ```
  - For Unix-based systems:
    ```sh
    source venv/bin/activate
    ```
3. Change directory into the project:
   ```sh
   cd shop-backend
   ```
4. Install dependencies:
   ```sh
   pip3 install -r requirements.txt
   ```
5. Set your environment variables:
   ```sh
   cp .env-sample .env
   ```
6. Run:
   ```sh
   python3 manage.py migrate
   python3 manage.py runserver
   ```
