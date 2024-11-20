from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'users',
    'cabinet',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'barbershop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'barbershop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'
# TIME_ZONE = 'Europe/Kaliningrad'      # Калининград (UTC+2)
# TIME_ZONE = 'Europe/Moscow'           # Москва, центр (UTC+3)
# TIME_ZONE = 'Europe/Samara'           # Самара (UTC+4)
# TIME_ZONE = 'Asia/Yekaterinburg'      # Екатеринбург (UTC+5)
# TIME_ZONE = 'Asia/Omsk'               # Омск (UTC+6)
# TIME_ZONE = 'Asia/Novosibirsk'        # Новосибирск (UTC+7)
# TIME_ZONE = 'Asia/Krasnoyarsk'        # Красноярск (UTC+7)
# TIME_ZONE = 'Asia/Irkutsk'            # Иркутск (UTC+8)
# TIME_ZONE = 'Asia/Yakutsk'            # Якутск (UTC+9)
# TIME_ZONE = 'Asia/Vladivostok'        # Владивосток (UTC+10)
# TIME_ZONE = 'Asia/Magadan'            # Магадан (UTC+11)
# TIME_ZONE = 'Asia/Kamchatka'          # Петропавловск-Камчатский (UTC+12)
# TIME_ZONE = 'Asia/Almaty'             # Астана/Алматы (UTC+6)


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Конфигурация для отправки уведомлений в Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
YOUR_PERSONAL_CHAT_ID = os.getenv("YOUR_PERSONAL_CHAT_ID")


# JAZZMIN_SETTINGS = {
#     "site_title": "Название сайта",
#     "site_header": "Название в шапке",
#     "site_brand": "Ирина",
#     "welcome_sign": "Добро пожаловать в админ-панель",
#     "copyright": "Acme Ltd",
#     "login_logo": "Путь к логотипу, который будет отображаться на странице входа",
#     "login_background": "Путь к фоновому изображению на странице входа",
#     "show_sidebar": "Отображать или скрывать боковую панель (по умолчанию True)",
#     "navigation_expanded": "Раскрывать ли навигацию по умолчанию (по умолчанию False)",
#     "user_avatar": "Путь к аватару пользователя, отображаемому в правом верхнем углу",
#     "custom_css": "Путь к вашему собственному CSS-файлу для кастомизации стилей админки",
#     "custom_js": "Путь к вашему собственному JavaScript-файлу для добавления функционала",
#     "language_chooser": "Включить выбор языка в админке (по умолчанию True)",
#     "icons": "Настройка иконок для моделей и других элементов интерфейса",
#     "disable_jazzmin": "Отключить Jazzmin (по умолчанию False)",
# }

JAZZMIN_SETTINGS = {
    "site_title": 'Барбершоп "Ирина"',
    "site_header": 'Барбершоп "Ирина"',
    "site_brand": '"Ирина"',
    "welcome_sign": "Добро пожаловать в админ-панель",
    "copyright": 'Моё домашнее задание на 26-27.11.2024'
}

AUTH_USER_MODEL = 'users.CustomUser'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
