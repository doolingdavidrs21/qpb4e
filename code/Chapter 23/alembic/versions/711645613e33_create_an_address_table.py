"""create an address table

Revision ID: 711645613e33
Revises: eeea36c2a47c
Create Date: 2026-01-20 12:45:37.121336

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '711645613e33'
down_revision: Union[str, Sequence[str], None] = 'eeea36c2a47c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
