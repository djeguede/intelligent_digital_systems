# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa

from app.models.exemple import Exemple
from app.models.user import User
from app.models.role import Role

