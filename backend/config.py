import os

BASE_DIR = os.path.abspath(os.path.dirname(**file**))

class Config:
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")

```
JWT_SECRET_KEY = os.environ.get(
    "JWT_SECRET_KEY",
    "dev-jwt-secret-change-me"
)

SQLALCHEMY_DATABASE_URI = (
    "sqlite:///" + os.path.join(BASE_DIR, "gridlink.db")
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
```
