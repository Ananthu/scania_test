from fastapi import APIRouter, Depends, HTTPException
from ..services.cost_calculator import CostCalculatorService
from ..dependencies import get_cost_calculator_service

router = APIRouter()

@router.get("/zoo/food_costs")
def food_costs(service: CostCalculatorService = Depends(get_cost_calculator_service)) -> dict:
    """
    Endpoint to calculate the total cost of feeding all animals in the zoo.

    Utilizes the CostCalculatorService to sum the food costs based on dietary needs and current food prices.
    Service injection allows for flexible testing and adaptation to changes in calculation logic or data sources.

    Returns:
        A JSON object containing the 'total_food_cost'.

    Raises:
        HTTPException: Returns a 500 error if there's an issue during cost calculation.
    """
    try:
        return {"total_food_cost": service.calculate_food_costs()}
    except Exception:
        raise HTTPException(status_code=500, detail="An error occurred while calculating food costs.")
