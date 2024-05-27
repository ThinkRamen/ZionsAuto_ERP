from pathlib import Path
from dotenv import load_dotenv
import os
from google.cloud import storage
import json
from google.oauth2 import service_account


# Now you can use the `storage_client` to interact with Google Cloud Storage

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG")
print("Debug: ", DEBUG)
ALLOWED_HOSTS = ["127.0.0.1", ".vercel.app", "localhost", "10.0.0.93", "10.0.0.93:8000"]


# Application definition

INSTALLED_APPS = [
    "vehicles",
    "parts",
    "locations",
    "jobs",
    "advertisements",
    "appointments",
    "semantic_admin",
    "semantic_forms",
    "storages",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Zions_AutoERP.urls"
print(os.path.join(BASE_DIR, "templates/"))

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
    },
    "media": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
    },
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates/"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Zions_AutoERP.wsgi.app"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASS"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

## Google Cloud Storage Credentials
gcs_credentials = service_account.Credentials.from_service_account_info(
    json.loads(os.getenv("GOOGLE_SERVICE_KEY"))
)
### Set the Google Cloud Storage Bucket Name
GS_BUCKET_NAME = "zions-autoerp-static"
### Google Cloud Storage Configuration
GS_MEDIA_NAME = "zions-autoerp-media"
GS_CREDENTIALS = gcs_credentials
GS_PROJECT_ID = "zions-autoerp"

## Static and Media settings
STATIC_URL = os.path.join(BASE_DIR, "static/")
MEDIA_URL = os.path.join(BASE_DIR, "media/")

## Static and Media directories
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MAPS_API_KEY = os.getenv("MAPS_API_KEY")
