class AccountExecutive:
    def __init__(self,name,salary,years_experience):
        self.name = name
        self.salary = salary
        self.years_experience = years_experience

    def __repr__(self,name,salary,years_experience):
        return "Class AccountExecutive{name:{},salary:{},years_experience:{}".format(self.name,self.salary,self.years_experience)

def giveraise(x):
    total_raise_percentage = .1
    raise_ammount = .1 * float(x)
    new_comp = raise_ammount + x
    return new_comp




Chris_Murray = AccountExecutive(name="Chris Murray",salary=95000,years_experience=1)
Daniel_Leish= AccountExecutive(name="Daniel_Leish",salary=95000,years_experience=3)
Andres_Arce = AccountExecutive(name="Andres Arce",salary=85000,years_experience=1)

list_ae = []
list_ae.append(Chris_Murray)
list_ae.append(Andres_Arce)
list_ae.append(Chris_Murray)

ae_after_raise = [giveraise(x) for x in list_ae]

