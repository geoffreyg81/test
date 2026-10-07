class VehicleError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
    def __repr__(self) -> str:
        return self.message
class MotorisationError(VehicleError):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
    def __repr__(self) -> str:
        return self.message