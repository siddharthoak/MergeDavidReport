class BluepageUser:
    def __init__(self, name, expiry_date, manager_name, email):
        self.name = name
        self.expiry_date = expiry_date.strftime("%m/%d/%Y")
        self.manager_name = manager_name
        self.email = email

    def __str__(self):
        retstr= self.name + "--" + self.expiry_date + "--" + self.manager_name+" -- "+self.email
        return retstr