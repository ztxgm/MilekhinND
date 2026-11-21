import logging

from fastapi import APIRouter, HTTPException, Path, Query
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/items", tags=["items"])

fake_db = {1: {"name": "Foo", "price": 50.2}}


class Item(BaseModel):
    name: str = Field(..., title="Название", examples=["Телефон"])
    price: float = Field(..., gt=0, title="Цена", examples=[199.99])
    is_offer: bool | None = Field(None, title="Акционный товар")


def name_exists(name: str, exclude_id: int | None = None) -> bool:
    return any(
        data["name"].lower() == name.lower()
        for item_id, data in fake_db.items()
        if item_id != exclude_id
    )


@router.get("/{item_id}", summary="Получить товар по ID")
def read_item(
    item_id: int = Path(..., title="ID товара", ge=1),
    q: str | None = Query(None, title="Поисковый запрос", max_length=50),
):
    if item_id not in fake_db:
        logger.warning("Товар %s не найден", item_id)
        raise HTTPException(status_code=404, detail="Item not found")
    logger.info("Запрошен товар %s", item_id)
    return {"item_id": item_id, "item": fake_db[item_id], "q": q}


@router.post("/", response_model=Item, summary="Создать товар")
def create_item(item: Item):
    if name_exists(item.name):
        logger.warning("Дубликат имени товара: %s", item.name)
        raise HTTPException(status_code=409, detail="Item name must be unique")
    new_id = max(fake_db, default=0) + 1
    fake_db[new_id] = item.model_dump()
    logger.info("Создан товар %s: %s", new_id, item.name)
    return item


@router.put("/{item_id}", response_model=Item, summary="Обновить товар")
def update_item(
    item: Item,
    item_id: int = Path(..., title="ID товара", ge=1),
):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    if name_exists(item.name, exclude_id=item_id):
        raise HTTPException(status_code=409, detail="Item name must be unique")
    fake_db[item_id] = item.model_dump()
    logger.info("Обновлён товар %s", item_id)
    return item
