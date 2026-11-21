from fastapi import APIRouter, HTTPException, Path, Query
from pydantic import BaseModel, Field

router = APIRouter(prefix="/items", tags=["items"])

fake_db = {1: {"name": "Foo", "price": 50.2}}


class Item(BaseModel):
    name: str = Field(..., title="Название", examples=["Телефон"])
    price: float = Field(..., gt=0, title="Цена", examples=[199.99])
    is_offer: bool | None = Field(None, title="Акционный товар")


@router.get("/{item_id}", summary="Получить товар по ID")
def read_item(
    item_id: int = Path(..., title="ID товара", ge=1),
    q: str | None = Query(None, title="Поисковый запрос", max_length=50),
):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item": fake_db[item_id], "q": q}


@router.post("/", response_model=Item, summary="Создать товар")
def create_item(item: Item):
    return item
