# Photography Portfolio Website
# موقع محفظة التصوير الفوتوغرافي

## Features / المميزات 
- Responsive Design 
- Photo Gallery / معرض الصور 
- Category Filtering / تصفية الفئات 
- Contact Form / نموذج الاتصال 
- Admin Panel / لوحة التحكم 
- REST API / واجهة برمجة التطبيقات / REST API

## Setup Instructions / تعليمات الإعداد 

### Requirements / المتطلبات 
- Python 3.8 or higher
- Django 4.2
- Django REST framework
- Pillow
- django-cors-headers
- python-dotenv

### Installation / التثبيت 
1. Clone the repository / استنساخ المستودع 
```bash
git clone https://github.com/alameed143/photography-portfolio.git
cd photography-portfolio
```

2. Create virtual environment / إنشاء بيئة افتراضية 
```bash
python -m venv venv
```

3. Activate virtual environment / تفعيل البيئة الافتراضية 
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install dependencies / تثبيت التبعيات / डिपेंडेंसी इंस्टॉल करें:
```bash
pip install -r requirements.txt
```

5. Run migrations / تشغيل الترحيلات / माइग्रेशन चलाएं:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser / إنشاء مستخدم رئيسي / सुपरयूजर बनाएं:
```bash
python manage.py createsuperuser
```

7. Run the server / تشغيل الخادم / सर्वर चलाएं:
```bash
python manage.py runserver
```

### Access Points / نقاط الوصول 
- Website: http://localhost:8000/
- Admin Panel: http://localhost:8000/admin/
- API Endpoints:
  - Photos: http://localhost:8000/api/photos/
  - Categories: http://localhost:8000/api/categories/

## Project Structure / هيكل المشروع 
```
photography-portfolio/
├── frontend/
│   ├── static/
│   │   └── frontend/
│   │       ├── css/
│   │       └── js/
│   └── templates/
│       └── frontend/
├── photos/
│   ├── migrations/
│   ├── models.py
│   └── views.py
├── portfolio_backend/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── .env
```

## Contributing / المساهمة 
Feel free to contribute to this project by:
- Creating issues
- Submitting pull requests
- Improving documentation

## License / الترخيص / लाइसेंस
This project is licensed under the MIT License.
