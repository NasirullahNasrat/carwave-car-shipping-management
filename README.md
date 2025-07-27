# 🚗 Carwave Vehicle Management System  

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A comprehensive vehicle lifecycle management system built with Django, featuring multi-currency support and complete tracking from purchase to sale.

## 🌟 Key Features

| Feature | Description |
|---------|-------------|
| 💰 Multi-Currency | Track expenses in multiple currencies with auto-conversion to USD |
| 📦 Full Lifecycle | Manage vehicles from purchase through shipping to final sale |
| 📊 Financial Tracking | Detailed cost breakdowns and profit/loss calculations |
| 🌍 International | Designed for Persian language but fully adaptable |
| 📈 Reporting | Automatic calculations at each stage of the process |

## 🛠️ Tech Stack

- **Backend**: Django 4.x
- **Database**: PostgreSQL (SQLite for development)
- **Frontend**: Django Templates + Bootstrap
- **Deployment**: Docker-ready (coming soon)

## 📸 Screenshots

![Sample Interface]
https://raw.githubusercontent.com/NasirullahNasrat/carwave-car-shipping-management/refs/heads/main/project_images/1.png

## 🚀 Installation

### Prerequisites
- Python 3.10+
- PostgreSQL
- pip

### Quick Start
```bash
# Clone repository
git clone https://github.com/yourusername/vehicle-management-system.git
cd vehicle-management-system

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure settings
settings.py

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run development server
python manage.py runserver


Access the system at http://localhost:8000

🧠 What I Learned
✅ Building complex Django model relationships
✅ Implementing custom model fields and mixins
✅ Financial calculations with currency conversion
✅ Multi-stage workflow implementation
✅ Persian language RTL support in Django
✅ Automated historical data tracking

🧗 Challenges Overcome
Challenge	Solution
Complex currency conversions	Created CurrencyModelMixin for consistent handling
Multi-stage cost tracking	Implemented cumulative calculation properties
Persian date handling	Custom form fields and template filters
Data validation	Extensive model clean() methods

📜 License
Distributed under the Apache License. 

📬 Contact
Nasirullah Nasrat - nasirullahnasrat93@gmail.com
