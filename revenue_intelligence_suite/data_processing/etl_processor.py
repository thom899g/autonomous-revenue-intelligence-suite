from typing import Dict, Any
import logging

class ETLProcessor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def clean_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            # Data cleaning logic
            cleaned = {}
            if 'revenue' in data and isinstance(data['revenue'], (int, float)):
                cleaned['revenue'] = data['revenue']
            return cleaned
        except Exception as e:
            self.logger.error(f"Data cleaning failed: {e}")
            raise

    def transform_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            # Data transformation logic
            transformed = {
                'monthly_growth': (data['revenue'] / 12),
                'expense_ratio': (data['expenses'] / data['revenue'])
            }
            return transformed
        except KeyError as e:
            self.logger.error(f"Missing key: {e}")
            raise

    def process_data(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        cleaned = self.clean_data(raw_data)
        transformed = self.transform_data(cleaned)
        return transformed