class BaseModel:
    def get_id(self):
        return self.key().id()

    def get_type(self):
        return self.kind()

