from src.core.entities.contacts import Contact
from src.core.enum.active import ActiveCondition
from src.core.enum.status import Status
from src.repository.util.contacts import ContactsRepository


class GetContactDetailsContactsRepository(ContactsRepository):
    def get(self, identity: str) -> Contact:
        contact_detail_as_json = self.find_one(identity, ActiveCondition.ACTIVE.value)
        contact_detail = self._transform_from_json_to_contact(contact_detail_as_json)
        return contact_detail

