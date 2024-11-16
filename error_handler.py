class SQLError(Exception):
    """
    Custom exception for SQL errors
    """

    def __init__(self, message="record not found"):
        self.message = message
        super().__init__(self.message)
