from src.core.interfaces.repository.i_redis_repository import IRedis


class SoftDeleteRegisters(IRedis):
    def verify_if_deleted_user_id(self, identification: str) -> bool:
        existe = self.verify_if_exists(identification)
        return not existe


