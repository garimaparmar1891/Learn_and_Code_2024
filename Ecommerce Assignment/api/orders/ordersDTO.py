from dataclasses import dataclass

@dataclass
class OrderResponseDTO:
    message: str
    order_id: int
    total_amount: float
    order_date: str

@dataclass
class OrderHistoryDTO:
    order_id: int
    order_date: str
    product_name: str
    quantity: int
    price: float
