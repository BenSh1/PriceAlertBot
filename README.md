# 🛒 Amazon Price Tracker Bot

A simple Python script that tracks the price of a product on Amazon (or other supported pages) and sends an email alert when the price drops below a defined threshold.

## 📦 Features

- Scrapes product price using `requests` and `BeautifulSoup`
- Sends email alerts via SMTP (e.g., Gmail)
- Uses `.env` file for secure credentials
- Customizable target price
- Headers mimic a real browser to avoid blocking

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/BenSh1/PriceAlertBot.git
cd PriceAlertBot
```

### 2. Set up virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

### 3.Install dependencies
Install dependencies
pip install -r requirements.txt

### 4. Create your .env file

MY_EMAIL=youremail@gmail.com
MY_PASSWORD=your_app_password
TO_EMAIL=recipientemail@gmail.com

📌 Important: Use a Gmail App Password if 2FA is enabled.


### 5. Run the script

python main.py


### 6.📬 Email Format
You'll receive an email like this when the price drops:

Subject: Instant Pot Price Alert!

The price has dropped!

Product: Instant Pot XYZ
Current Price: $95.00
Buy now: https://www.amazon.com/...