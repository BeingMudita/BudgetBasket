import enum


class PlatformEnum(str, enum.Enum):
    BLINKIT = "blinkit"
    ZEPTO = "zepto"
    INSTAMART = "instamart"
    BIGBASKET = "bigbasket"
    FLIPKART = "flipkart"
    AMAZON = "amazon"