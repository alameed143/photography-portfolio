# Photography Portfolio

A modern, responsive photography portfolio website built with Django and modern web technologies.

## Features

- **Dynamic Gallery**: Showcase your photography work with a beautiful, responsive gallery
- **Admin Dashboard**: Easy-to-use admin interface for managing your portfolio content
- **Site Settings**: Customize your site's appearance through the admin panel
- **Responsive Design**: Fully responsive layout that works on all devices
- **Modern UI**: Clean and professional design with smooth animations
- **Contact Form**: Built-in contact form for client inquiries

## Technology Stack

- **Backend**: Django 4.2
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default)
- **Additional Libraries**:
  - Django Rest Framework
  - WhiteNoise for static files
  - CORS headers
  - Django Filters

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alameed143/photography-portfolio.git
   cd photography_portfolio_backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
photography_portfolio_backend/
├── frontend/                 # Main application
│   ├── static/              # Static files (CSS, JS, images)
│   ├── templates/           # HTML templates
│   ├── models.py            # Database models
│   └── views.py             # View logic
├── photos/                  # Photo management app
├── manage.py               # Django management script
└── requirements.txt        # Project dependencies
```

## Usage

1. Access the admin panel at `http://127.0.0.1:8000/admin/`
2. Log in with your superuser credentials
3. Add your photos and content through the admin interface
4. Customize site settings as needed

## Navigation

- **Home**: Landing page with hero section
- **About**: Information about the photographer
- **Gallery**: Photo portfolio showcase
- **Contact**: Contact form for inquiries

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - [Your Email]
Project Link: https://github.com/alameed143/photography-portfolio
