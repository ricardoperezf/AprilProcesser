import os
from aprilprocesser import aprilprocesser_app, mongo

__author__ = "ricardoperezf"
__version__ = "1.0.0"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    aprilprocesser_app.run(host='0.0.0.0', port=port)
