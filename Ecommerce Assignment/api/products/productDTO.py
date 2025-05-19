from dataclasses import dataclass

@dataclass
class ProductDTO:
    name: str
    price: float
    quantity_available: int
