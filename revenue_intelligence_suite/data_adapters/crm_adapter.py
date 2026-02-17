from abc import ABC, abstractmethod
from typing import Dict, Any

class DataSourceAdapter(ABC):
    @abstractmethod
    def connect(self) -> bool:
        pass
    
    @abstractmethod
    def fetch_data(self, params: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def close(self) -> None:
        pass

class CRMAdapter(DataSourceAdapter):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self._connected = False
        
    def connect(self) -> bool:
        try:
            # Simulated connection logic
            if self.api_key:
                self._connected = True
                return True
            raise ValueError("API key is required")
        except Exception as e:
            print(f"Connection failed: {e}")
            return False

    def fetch_data(self, params: Dict[str, Any]) -> Dict[str, Any]:
        if not self._connected:
            raise ConnectionError("Not connected to CRM")
        # Simulated data retrieval
        return {
            "revenue": 100000,
            "expenses": 50000,
            "customers": 500
        }

    def close(self) -> None:
        self._connected = False