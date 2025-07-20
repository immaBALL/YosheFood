# YosheFood 🍕

A modern Django-based food ordering system with customer management and order processing capabilities.

## 🚀 Features

- **Customer Management**: Register and manage customer information
- **Food Ordering**: Browse and order food items
- **Order Processing**: Complete order workflow with confirmation
- **Guest Orders**: Support for guest customers without registration
- **Responsive Design**: Modern, mobile-friendly interface
- **Admin Panel**: Django admin interface for managing orders and customers

## 🛠️ Tech Stack

- **Backend**: Django 5.2.3
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Frontend**: HTML, CSS, JavaScript
- **Template Engine**: Django Templates
- **Static Files**: CSS styling with modern design

## 📋 Prerequisites

- Python 3.8+
- pip (Python package installer)
- Git

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/immaBALL/YosheFood.git
   cd YosheFood
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env file with your settings
   # Generate a new SECRET_KEY:
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Visit the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
YosheFood/
├── myapp/                 # Main Django application
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   ├── urls.py           # URL routing
│   └── admin.py          # Admin interface
├── templates/            # HTML templates
├── static/              # CSS, JS, and static files
├── media/               # User-uploaded files
├── myproject/           # Django project settings
└── requirements.txt     # Python dependencies
```

## 🎯 Usage

1. **For Customers:**
   - Visit the homepage to browse food items
   - Add items to your order
   - Provide customer details
   - Complete the order process

2. **For Administrators:**
   - Access the admin panel at `/admin/`
   - Manage orders, customers, and food items
   - View order history and customer information

## 🔒 Security Features

- Environment variable configuration for sensitive data
- CSRF protection enabled
- Secure password validation
- Proper file upload handling
- Comprehensive `.gitignore` to prevent sensitive data exposure

## 🚀 Deployment

For production deployment:

1. Set `DEBUG=False` in your environment variables
2. Configure a production database (PostgreSQL recommended)
3. Set up proper `ALLOWED_HOSTS`
4. Configure static file serving
5. Use HTTPS
6. Set up proper logging

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**immaBALL**
- GitHub: [@immaBALL](https://github.com/immaBALL)

## 🙏 Acknowledgments

- Django community for the excellent framework
- Contributors and testers
- Food ordering system inspiration

---

⭐ **Star this repository if you found it helpful!**
