import os
import sys
from alembic.config import Config
from alembic import command

def main():
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create Alembic config
    alembic_cfg = Config(os.path.join(script_dir, "alembic.ini"))
    
    # Run migrations
    command.upgrade(alembic_cfg, "head")

if __name__ == "__main__":
    main() 