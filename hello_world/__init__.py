from flask import Flask

app = Flask(__name__)

# Import views
from hello_world import views  # noqa: E402, F401