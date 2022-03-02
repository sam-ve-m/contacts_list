from src.core.interfaces.repository.i_mongo import IMongo


class Contacts(IMongo):
    DATABASE: str = "db_dif_2"
    COLLECTION: str = "col_dif_2"

