from pydantic import BaseModel


class ZeptoSearchResponse(BaseModel):
    success: bool
    platform: str
    query: str
    results: list