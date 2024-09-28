class TaxSystem():
    def __init__(self):
        self.rules = []
    
    def add_rule(self, condition, result):
        self.rules.append((condition, result))

    def apply_rules(self, input_value):
        for condition, result in self.rules:
            if condition(input_value):
                return result
        return "Default"
        
tax_system = TaxSystem()
tax_system.add_rule(lambda x: x <= 12570, "0%")
tax_system.add_rule(lambda x: 12571 <= x <= 50270, "20%")
tax_system.add_rule(lambda x: 50271 <= x <= 125140, "40%")
tax_system.add_rule(lambda x: x > 125140, "45%")

tax_rate = tax_system.apply_rules(60000)
print(tax_rate)