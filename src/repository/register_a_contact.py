from src.core.entities.contacts import Contact
from src.repository.util.contacts import ContactsRepository


class RegisterContactsRepository(ContactsRepository):
    def register(self, contact: Contact) -> bool:
        contact_as_json = self._transform_from_contact_to_json(contact)
        insert_status = self.insert_one(contact_as_json)
        return insert_status

