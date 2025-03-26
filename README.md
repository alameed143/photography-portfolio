# Photography Portfolio Website
# موقع محفظة التصوير الفوتوغرافي
# फोटोग्राफी पोर्टफोलियो वेबसाइट

## Features / المميزات / विशेषताएं
- Responsive Design / تصميم متجاوب / रेस्पॉन्सिव डिज़ाइन
- Photo Gallery / معرض الصور / फोटो गैलरी
- Category Filtering / تصفية الفئات / श्रेणी फ़िल्टरिंग
- Contact Form / نموذج الاتصال / संपर्क फॉर्म
- Admin Panel / لوحة التحكم / एडमिन पैनल
- REST API / واجهة برمجة التطبيقات / REST API

## Setup Instructions / تعليمات الإعداد / सेटअप निर्देश

### Requirements / المتطلبات / आवश्यकताएं
- Python 3.8 or higher
- Django 4.2
- Django REST framework
- Pillow
- django-cors-headers
- python-dotenv

### Installation / التثبيت / इंस्टॉलेशन
1. Clone the repository / استنساخ المستودع / रिपॉजिटरी क्लोन करें:
```bash
git clone https://github.com/alameed143/photography-portfolio.git
cd photography-portfolio
```

2. Create virtual environment / إنشاء بيئة افتراضية / वर्चुअल एनवायरनमेंट बनाएं:
```bash
python -m venv venv
```

3. Activate virtual environment / تفعيل البيئة الافتراضية / वर्चुअल एनवायरनमेंट सक्रिय करें:
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

### Access Points / نقاط الوصول / एक्सेस पॉइंट्स
- Website: http://localhost:8000/
- Admin Panel: http://localhost:8000/admin/
- API Endpoints:
  - Photos: http://localhost:8000/api/photos/
  - Categories: http://localhost:8000/api/categories/

## Project Structure / هيكل المشروع / प्रोजेक्ट संरचना
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

## Contributing / المساهمة / योगदान
Feel free to contribute to this project by:
- Creating issues
- Submitting pull requests
- Improving documentation

## License / الترخيص / लाइसेंस
This project is licensed under the MIT License. 