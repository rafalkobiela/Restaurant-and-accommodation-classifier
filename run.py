from app import app

from app.controllers import Predict, Score
from app.error_handler import handle_errors

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
