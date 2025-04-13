from typing import List, Dict, TypedDict


class BriefingState(TypedDict):
    subjects: List[str]
    current_index: int
    analyst_outputs: Dict[str, str]
    briefing: str
