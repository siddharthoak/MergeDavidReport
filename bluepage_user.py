class BluepageUser:
    def __init__(self, srno, lotus, name, manager_name, email, expiry_date):
        self.name = name
        self.srno = srno
        self.expiry_date = expiry_date #.strftime("%m/%d/%Y")
        self.manager_name = manager_name
        self.email = email
        self.lotus = lotus

    def __str__(self):
        retstr= self.name + "--" +  self.manager_name+" -- "+self.email
        return retstr