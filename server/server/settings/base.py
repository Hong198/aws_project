import os
from datetime import timedelta
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 필요한 디렉토리 생성 이미 존재해도 오류 발생 x
# os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "static"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "media"), exist_ok=True)

# env 파일 읽기
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, "env", "base.env"))

# logging settings # TODO: 나중에 추가
# LOGGING_NAME = env.str("LOGGING_NAME")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # djangorestframework
    "rest_framework",
    # djangorestframework-simplejwt
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",  # 토큰이 블랙리스트에 추가하여 만료되기전 토큰 비활성화
    # django-cors-headers
    "corsheaders",
    # drf-spectacular
    "drf_spectacular",
    # in app
    "users",
    "api",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# djangoresetframework
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        # "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.AllowAny",  # 모든 사용자가 인증 여부 관계 없이 API 접근 가능
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",  # drf-spectacular
    # "EXCEPTION_HANDLER": "config.exception_handler.custom_exception_handler",
}

# drf-spectacular / swagger
# link : https://drf-spectacular.readthedocs.io/en/latest/readme.html
SPECTACULAR_SETTINGS = {
    "TITLE": "Your Project API",  # 이름수정
    "DESCRIPTION": "Your project description",  # 설명 수정
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
}

# djangorestframework-simplejwt
SIMPLE_JWT = {
    # "SIGNING_KEY": env.str("SIGNING_KEY"), # 기본값은 SECRET_KEY
    "ACCESS_TOKEN_LIFETIME": timedelta(
        days=30
    ),  # TODO: 정해야 함 # 액세스 토큰의 유효 기간을 지정, 사용자 인증에 사용
    "REFRESH_TOKEN_LIFETIME": timedelta(
        days=90
    ),  # TODO: 정해야 함 # 리프레시 토큰 유효기간을 지정, 엑세스 토큰 갱신 할떄 사용
    "ROTATE_REFRESH_TOKENS": True,  # 리프레시 토큰이 사용될때마다 새로운 리프레시 토큰 발급, 기존 리프레시 토큰을 블랙리스트에 추가
    "BLACKLIST_AFTER_ROTATION": True,  # 사용된 리프레시 토큰 블랙리스트에 추가
    "UPDATE_LAST_LOGIN": True,  # 인증 선텍힐때마다 las_login필드 업데이트
    "ALGORITHM": "HS256",  # JWT 서명할때 알고리즘 지정
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    # "USER_ID_FIELD": "uid", # TODO: user 모델의 pk 필드명
    # "USER_ID_CLAIM": "user_uid" # TODO: claim에 추가할 변수명
}

# smtp send email
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"  # 사용할 이메일 서버의 호스트
# EMAIL_PORT = 587  # 이메일 서버의 포트
# EMAIL_USE_TLS = True  # TLS 사용 설정
# EMAIL_HOST_USER = env.str("EMAIL_HOST_USER")  # TODO: 이메일 계정(base.env 수정 필요)
# EMAIL_HOST_PASSWORD = env.str(
#     "EMAIL_HOST_PASSWORD"
# )  # TODO: 이메일 비밀번호(base.env 수정 필요)
# EMAIL_SUBJECT_PREFIX = env.str(
#     "EMAIL_SUBJECT_PREFIX"
# )  # TODO: 이메일 접두사(base.env 수정 필요)


# django-cors-headers
CORS_ALLOWED_ORIGINS = []


ROOT_URLCONF = "server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
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

WSGI_APPLICATION = "server.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

EDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# AUTH_USER_MODEL
AUTH_USER_MODEL = "users.CustomUser"
