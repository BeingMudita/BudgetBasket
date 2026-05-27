from app.integrations.base.client import BaseClient
from app.integrations.blinkit.constants import (
    BLINKIT_BASE_URL,
)


class BlinkitClient(BaseClient):
    BASE_URL = BLINKIT_BASE_URL