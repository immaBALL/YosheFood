# YosheFood - Django Food Ordering System

A modern food ordering web application built with Django, featuring a beautiful UI and secure order processing.

## Features

- 🍽️ Product catalog with images and pricing
- 🛒 Interactive order system with quantity controls
- 👤 Customer account management
- 📝 Order review and confirmation
- 🎨 Modern, responsive design
- 🔒 Secure checkout process

## Tech Stack

- **Backend**: Django 5.2.3
- **Database**: SQLite (development)
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Custom CSS with modern design
- **Environment**: Python 3.12+

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YosheFood.git
cd YosheFood
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the project root:

```bash
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings (if using external database)
# DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Email Settings (if using email functionality)
# EMAIL_HOST=smtp.gmail.com
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER=your-email@gmail.com
# EMAIL_HOST_PASSWORD=your-app-password
```

### 5. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the application.

## Project Structure

```
myproject/
├── myapp/                 # Main Django application
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   ├── urls.py           # URL routing
│   └── admin.py          # Admin interface
├── myproject/            # Django project settings
│   ├── settings.py       # Project configuration
│   └── urls.py           # Main URL routing
├── templates/            # HTML templates
├── static/               # Static files (CSS, JS)
├── media/                # User-uploaded files
├── .env                  # Environment variables (not in git)
├── .gitignore           # Git ignore patterns
└── requirements.txt     # Python dependencies
```

## Security Features

- ✅ Environment variables for sensitive data
- ✅ Django's built-in CSRF protection
- ✅ SQL injection protection
- ✅ XSS protection
- ✅ Secure form handling
- ✅ Input validation and sanitization

## Development Guidelines

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add comments for complex logic

### Git Workflow
1. Create feature branches for new development
2. Commit frequently with descriptive messages
3. Never commit sensitive data or credentials
4. Review changes before merging

### Environment Variables
- Never commit `.env` files to version control
- Use environment variables for all sensitive configuration
- Document required environment variables in README

## Deployment

### Production Checklist
- [ ] Set `DEBUG=False` in production
- [ ] Use a production database (PostgreSQL recommended)
- [ ] Configure proper `ALLOWED_HOSTS`
- [ ] Set up static file serving
- [ ] Configure HTTPS
- [ ] Set up proper logging
- [ ] Use environment variables for all secrets

### Recommended Hosting
- **Heroku**: Easy deployment with PostgreSQL
- **DigitalOcean**: Full control with App Platform
- **AWS**: Scalable with Elastic Beanstalk
- **Vercel**: Fast deployment with serverless functions

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support and questions:
- Create an issue on GitHub
- Contact: [your-email@example.com]

## Acknowledgments

- Django community for the excellent framework
- Icons8 for the meal icon
- Google Fonts for typography 