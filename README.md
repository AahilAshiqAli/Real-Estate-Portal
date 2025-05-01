# 🏡 EliteEstateRoyce - Real Estate Listing Platform

EliteEstateRoyce is a Django-based real estate platform where users can:

- 🏘️ View all house listings
- 📄 Click into individual house details
- 📞 Contact for inquiries
- 🌐 Land on a beautiful front page
- 🔍 Filter listings by city, price range, and more



## 📂 Features

- **Listings Page** – Displays all available homes.
- **Description Page** – Detailed view of a selected house.
- **Contact Page** – Lets users submit inquiries.
- **Front Page** – The home landing page.
- **Filtering** – Easily narrow down homes based on your preferences.



## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/elite-estate-royce.git
cd elite-estate-royce
```

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 1. Configure the Database
Open settings.py in your project folder and edit the DATABASES section:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # or your DB engine
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 1. Update Models
Inside polls/models.py, make sure the EliteEstateRoyce model has:
```bash
class Meta:
    managed = False
```

### 1. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```


### 1. Start the Development Server

```bash
python manage.py runserver
```


SRS s attahed for reference
