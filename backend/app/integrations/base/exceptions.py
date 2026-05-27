class IntegrationError(Exception):
    pass


class PlatformUnavailableError(IntegrationError):
    pass


class ProductNotFoundError(IntegrationError):
    pass