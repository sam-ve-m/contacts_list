from typing import List, Iterator

from src.core.entities.contacts import Contact
from src.repository.util.contacts import ContactsRepository


class GetContactListContactsRepository(ContactsRepository):
    def get(self) -> List[Contact]:
        list_of_contacts: Iterator[dict] = self.find_all()
        list_of_contacts_return = [
            self._transform_from_json_to_contact(contact_as_json)
            for contact_as_json in list_of_contacts
        ]
        return list_of_contacts_return

