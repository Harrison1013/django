class NoSpecifyBrowser(Exception):
    def __init__(self, error_info):
        super().__init__(self)  # 初始化父頻
        self.error_info = error_info

    def __str__(self):
        return self.error_info


class NoSuchMethod(Exception):
    def __init__(self, error_info):
        super().__init__(self)  # 初始化父頻
        self.error_info = error_info

    def __str__(self):
        return self.error_info


class RequestFail(Exception):
    def __init__(self, error_info):
        super().__init__(self)  # 初始化父頻
        self.error_info = error_info

    def __str__(self):
        return self.error_info
