def diet_change(size, weight_status):
    diet_plan = []

    if weight_status == "overweight":
        hay_answer = input("Do you give unlimited hay? (y/n) ")
        if hay_answer.lower() == "n":
            diet_plan.append("Give unlimited hay! Bunnies need unlimited hay for good digestion and weight control.")

        try:
            pellets = float(input("How many cups of pellets do you feed daily? "))
            if size == "small" and pellets > 0.125:
                diet_plan.append(f"Cut back pellets from {pellets} cups to just 1/8 cup (2 tbsp) each day.")
            elif size == "medium" and pellets > 0.25:
                diet_plan.append(f"Reduce pellets from {pellets} cups to 1/4 cup daily.")
            elif (size == "large" or size == "giant") and pellets > 0.5:
                diet_plan.append(f"Cut pellets from {pellets} cups to 1/2 cup each day.")
        except ValueError:
            diet_plan.append("I need a real number for pellets.")

        try:
            greens = float(input("How many cups of leafy greens each day? "))
            if size == "small":
                if greens < 1:
                    diet_plan.append(f"More greens! Go from {greens} cups to 1 cup daily.")
                elif greens > 2:
                    diet_plan.append(f"Too many greens. Cut from {greens} cups to 1-2 cups daily.")
            elif size == "medium":
                if greens < 2:
                    diet_plan.append(f"More greens needed - from {greens} cups to 2 cups daily.")
                elif greens > 3:
                    diet_plan.append(f"Too many greens. Go from {greens} cups to 2-3 cups daily.")
            else:  # large or giant
                if greens < 3:
                    diet_plan.append(f"Bump up greens from {greens} cups to 3 cups daily.")
                elif greens > 5:
                    diet_plan.append(f"Cut back greens from {greens} cups to 3-5 cups.")
        except ValueError:
            diet_plan.append("Need a real number for greens.")

        try:
            treats = int(input("How many treats per day? "))
            if treats > 1:
                diet_plan.append(f"Too many treats! Cut from {treats} to just 1 small treat or none while slimming down.")
        except ValueError:
            diet_plan.append("Need a number for treats.")

        diet_plan.append("Get your bunny moving! 30 more minutes of exercise daily.")

    elif weight_status == "underweight":
        diet_plan.append("Keep hay available 24/7.")

        if size == "small":
            diet_plan.append("More pellets - give 1/4 cup daily.")
        elif size == "medium":
            diet_plan.append("Bump up pellets to 1/3 cup daily.")
        else:  # large or giant
            diet_plan.append("Increase pellets to 3/4 cup daily.")

        try:
            greens = float(input("How many cups of leafy greens daily? "))
            if size == "small" and greens < 1:
                diet_plan.append(f"More greens! Go from {greens} cups to 1-2 cups daily.")
            elif size == "medium" and greens < 2:
                diet_plan.append(f"Up the greens from {greens} cups to 2-3 cups daily.")
            elif (size == "large" or size == "giant") and greens < 3:
                diet_plan.append(f"More greens - from {greens} cups to 3-4 cups daily.")
        except ValueError:
            diet_plan.append("Need a real number for greens.")

        try:
            treats = int(input("Treats per day? "))
            if treats < 2:
                diet_plan.append("Can offer up to 2 nutritious treats daily while gaining weight.")
        except ValueError:
            diet_plan.append("Need a number for treats.")

        diet_plan.append("Add some alfalfa hay - yes, even for adults.")
        diet_plan.append("Try a tiny bit of oats (1 tsp daily).")
        diet_plan.append("See the vet to check for health problems.")

    else:  # normal weight
        diet_plan.append("Current feeding looks good - keep it up.")

        if size == "small":
            diet_plan.append("Keep pellets at 1/8 cup (2 tbsp) daily.")
        elif size == "medium":
            diet_plan.append("Stay with 1/4 cup pellets daily.")
        else:  # large or giant
            diet_plan.append("Keep giving 1/2 cup pellets daily.")

        try:
            greens = float(input("How many cups of leafy greens daily? "))
            if size == "small":
                if greens < 1:
                    diet_plan.append(f"Need more greens - go from {greens} cups to 1-2 cups.")
                elif greens > 2:
                    diet_plan.append(f"Too many greens - drop from {greens} cups to 1-2 cups.")
            elif size == "medium":
                if greens < 2:
                    diet_plan.append(f"Not enough greens - increase from {greens} cups to 2-3 cups.")
                elif greens > 3:
                    diet_plan.append(f"Cut back greens from {greens} cups to 2-3 cups.")
            else:  # large or giant
                if greens < 3:
                    diet_plan.append(f"Bump up greens from {greens} cups to 3-4 cups.")
                elif greens > 4:
                    diet_plan.append(f"Too many greens - drop from {greens} cups to 3-4 cups.")
        except ValueError:
            diet_plan.append("Need a real number for greens.")

        try:
            treats = int(input("Treats per day? "))
            if treats > 2:
                diet_plan.append(f"Too many treats! Go from {treats} down to 1-2 small treats daily.")
        except ValueError:
            diet_plan.append("Need a number for treats.")

        diet_plan.append("Keep unlimited hay available always.")

    print("\n--- BUNNY DIET PLAN ---")
    for recommendation in diet_plan:
        print(recommendation)
    print("\nMake changes slowly to avoid tummy troubles.")
    print("Always check with your vet before big diet changes.")

def breedcheck():
    size = input("Is your bunny small, medium, large, or giant sized? \nSmall: Netherland Dwarf, Jersey Wooly (1-5 lbs)\nMedium: Dutch, Dwarf Lop (6-9lbs)\nLarge: English Lop (9-11 lbs)\nGiant: Flemish Giant (11+ lbs)\n> ").lower()

    if size not in ["small", "medium", "large", "giant"]:
        print("That's not a valid size. Try again.")
        return breedcheck()

    weight_status = input("Is your bunny above weight, below weight, or average for their size? (above/below/average)\n> ").lower()

    if weight_status == "above":
        diet_change(size, "overweight")
    elif weight_status == "below":
        diet_change(size, "underweight")
    else:
        diet_change(size, "normal")

def homepage():
    print("CarrotCounter v1.0.0")
    print('By: Patrick Lee, Maxim Klochkov, Wesley Liu')
    print("DISCLAIMER: This is just for guidance. Always check with a vet before changing your bunny's diet")
    print("\n")
    print("Double check everything to be safe.")

    if input("Ready to start? (y/n) ").lower() == "y":
        breedcheck()
    else:
        print("Thanks for using CarrotCounter!")

if __name__ == "__main__":
    homepage()
