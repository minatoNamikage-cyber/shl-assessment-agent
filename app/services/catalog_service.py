import json
from pathlib import Path
from typing import List, Optional

from app.models.catalog import CatalogItem
from app.core.logging import logger


class CatalogService:
    """
    Service responsible for loading and providing
    access to SHL assessment catalog.
    """

    def __init__(self):
        self._catalog: List[CatalogItem] = []
        self._loaded: bool = False

    def load_catalog(self) -> None:
        """
        Load catalog from JSON file into memory.
        """

        if self._loaded:
            logger.info("Catalog already loaded.")
            return

        catalog_path = Path("app/data/catalog.json")

        if not catalog_path.exists():
            raise FileNotFoundError(
                f"Catalog file not found: {catalog_path}"
            )

        logger.info("Loading SHL catalog...")

        with open(catalog_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self._catalog = [
            CatalogItem(**item)
            for item in data
            if item.get("status", "ok") == "ok"
        ]

        self._loaded = True

        logger.success(
            f"Loaded {len(self._catalog)} assessments."
        )

    def get_all(self) -> List[CatalogItem]:
        return self._catalog

    def get_by_id(self, entity_id: str) -> Optional[CatalogItem]:

        for assessment in self._catalog:
            if assessment.entity_id == entity_id:
                return assessment

        return None

    def get_by_name(self, name: str) -> Optional[CatalogItem]:

        name = name.lower()

        for assessment in self._catalog:

            if assessment.name.lower() == name:
                return assessment

        return None

    @property
    def total_assessments(self) -> int:
        return len(self._catalog)

    @property
    def is_loaded(self) -> bool:
        return self._loaded


catalog_service = CatalogService()