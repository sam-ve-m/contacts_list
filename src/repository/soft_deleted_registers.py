from src.core.entities.contacts import Contact
from src.core.interfaces.repository.i_redis_repository import IRedis


class SoftDeleteRegisters(IRedis):
    def verify_if_contact_was_deleted(self, contact: Contact) -> bool:
        contact_id = contact.contactId
        exists = self.verify_if_exists(contact_id)
        return exists
