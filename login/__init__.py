from .login import login_blueprint
from .verify import verify_blueprint
from .register import register_blueprint


blueprint = [
  login_blueprint,
  verify_blueprint,
  register_blueprint,


]