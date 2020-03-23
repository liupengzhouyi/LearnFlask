from .login import login_blueprint
from .verify import verify_blueprint

blueprint = [
  login_blueprint,
  verify_blueprint,

]