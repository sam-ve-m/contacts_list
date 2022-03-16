from typing import Tuple

from src.core.entities.active import Active
from src.core.entities.address import Address
from src.core.entities.name import Name
from src.repository.util.contacts import ContactsRepository


class UpdateContactRepository(ContactsRepository):
    def update_contact(self, contact_id: str, updates: Tuple[Name, Address, Active]) -> bool:
        updates_per_entity_methods = {
            Name: ...,
            Address: lambda entity_Address: {"address": entity_Address.full_address},
            Active: lambda entity_Active: {"active": entity_Active.is_active},
        }
        updates_json = {}
        for unique_update in updates:
            update_method = updates_per_entity_methods.get(type(unique_update))
            unique_update_json: dict = update_method(unique_update)
            updates_json.update(unique_update_json)
        return self.update_one(contact_id, updates_json)
