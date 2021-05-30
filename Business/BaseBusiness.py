class BaseBusiness:
    def save(self, obj):
        self.validate_save(obj)
        self.before_save(obj)
        self.saving(obj)
        self.after_save(obj)

    def get_all(self):
        pass

    def validate_save(self, obj):
        pass

    def before_save(self, obj):
        pass

    def saving(self, obj):
        pass

    def after_save(self, obj):
        pass
