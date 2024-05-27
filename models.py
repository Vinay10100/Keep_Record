class CompanyRecord:
    def __init__(self, name, role, package, shortlisted, given_interview, final_result):
        self.name = name
        self.role = role
        self.package = package
        self.shortlisted = shortlisted
        self.given_interview = given_interview
        self.final_result = final_result

    def to_dict(self):
        return {
            "name": self.name,
            "role": self.role,
            "package": self.package,
            "shortlisted": self.shortlisted,
            "given_interview": self.given_interview,
            "final_result": self.final_result,
        }
