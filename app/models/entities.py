from pydantic import BaseModel

class TotalCostResponse(BaseModel):
    total_food_cost: float
