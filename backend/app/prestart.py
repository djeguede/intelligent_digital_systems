#/**
# Create data base migration
# **/
import subprocess
import sys, os
from pathlib import Path

from alembic.config import Config
from alembic import command

from app.core.config import ROOT


print(f'>>>>> {str(ROOT.parent / "alembic.ini")} ')
alembic_cfg = Config( str(ROOT.parent / "alembic.ini") )
alembic_cfg.set_main_option('script_location', str(ROOT.parent / "alembic"))
print(f'>>>>> SQLALCHEMY_DATABASE_URI: {os.environ.get("SQLALCHEMY_DATABASE_URI")}')
alembic_cfg.set_main_option('sqlalchemy.url', os.environ.get("SQLALCHEMY_DATABASE_URI"))

subprocess.run([sys.executable, "./app/backend_pre_start.py"])
command.revision(alembic_cfg, "--autogenerate")  # Generate new migration file
command.upgrade(alembic_cfg, "head")
subprocess.run([sys.executable, "./app/initial_data.py"])
