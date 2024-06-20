from .base import *
import environ

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, "env", "development.env"))

DEBUG = True
ALLOWED_HOSTS = ["*"]
