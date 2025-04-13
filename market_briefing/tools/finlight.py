from langchain.tools import StructuredTool
from finlight_client import FinlightApi
from finlight_client.models import ApiResponse
from pydantic import BaseModel, Field

from market_briefing.config import FINLIGHT_API_KEY


class GetBasicArticle(BaseModel):
    query: str = Field(..., description="Search term, e.g., 'Nvidia'")
    from_: str = Field(..., alias="from", description="ISO 8601 start time")
    to: str = Field(..., description="ISO 8601 end time")
    pageSize: int = Field(100, description="Number of articles per page")
    page: int = Field(1, description="Page number")


def search_finlight_articles(params: GetBasicArticle) -> str:
    client = FinlightApi(config={"api_key": FINLIGHT_API_KEY})
    param_dict = params.model_dump(by_alias=True)
    api_response: ApiResponse = client.articles.get_basic_articles(params=param_dict)

    if not api_response:
        return "No articles found."

    return "\n".join(
        f"Title: {a['title']}\nDate: {a['publishDate']}\nSummary: {a['summary'] or 'No summary.'}\n{'-'*30}"
        for a in api_response["articles"]
    )


search_tool = StructuredTool.from_function(
    func=search_finlight_articles,
    name="search_finlight_articles",
    description="Search Finlight for news by keyword and date range",
)
