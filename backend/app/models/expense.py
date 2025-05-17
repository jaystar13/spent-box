from pydantic import BaseModel, conint
from typing import List
from typing import Annotated

PositiveInt = Annotated[int, conint(ge=0)]
YearType = Annotated[int, conint(ge=2000, le=2100)]
MonthType = Annotated[int, conint(ge=1, le=12)]


class ExpenseItem(BaseModel):
    category: str
    amount: PositiveInt


class MonthlyExpenseRequest(BaseModel):
    year: YearType
    month: MonthType
    expenses: List[ExpenseItem]


class MonthlyExpenses(BaseModel):
    year: YearType
    month: MonthType
    expenses: List[ExpenseItem]


class MonthlyExpenseResponse(BaseModel):
    message: str
    data: MonthlyExpenses
