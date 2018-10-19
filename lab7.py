import lsystems

def main():

    axiom = input("Please enter the axiom: ")
    num_iter = int(input("Please enter the number of iterations: "))
    angle = int(input("Please enter the angle: "))
    distance = int(input("Please enter the distance: "))
    num_rules = int(input("Please enter the number of rules: "))
    rulesList = []
    for i in range(num_rules):
        rule = input("Please enter the rule in the format character:substitution")
        rulesList.insert(0, rule)
    lsystems.drawLSystem(lsystems.createLSystem(num_iter, axiom, rulesList), distance, angle)


main()

