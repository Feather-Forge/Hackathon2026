def diet_change(size, weight_status):
    # Start with empty list to collect diet recommendations
    diet_plan = []

    if weight_status == "overweight":
        diet_plan.extend(handle_overweight_bunny(size))
    elif weight_status == "underweight":
        diet_plan.extend(handle_underweight_bunny(size))
    else:  # normal weight
        diet_plan.extend(handle_normal_weight_bunny(size))

    # final plan
    print("\n--- BUNNY DIET PLAN ---")
    for recommendation in diet_plan:
        print(recommendation)
    print("\nMake changes slowly to avoid tummy troubles.")
    print("Always check with your vet before big diet changes.")


def handle_overweight_bunny(size):
    diet_plan = []

    # check hay
    diet_plan.extend(check_hay_for_overweight())

    # check pellets
    diet_plan.extend(check_pellets_for_overweight(size))

    # check greens
    diet_plan.extend(check_greens_for_overweight(size))

    # limit treats
    diet_plan.extend(check_treats_for_overweight())

    # Exercise is important for weight loss
    diet_plan.append("Get your bunny moving! 30 more minutes of exercise daily.")

    return diet_plan


def check_hay_for_overweight():
    diet_plan = []
    hay_answer = input("Do you give unlimited hay? (y/n) ")
    if hay_answer.lower() == "n":
        diet_plan.append("Give unlimited hay! Bunnies need unlimited hay for good digestion and weight control.")
    return diet_plan


def check_pellets_for_overweight(size):
    diet_plan = []
    try:
        pellets = float(input("How many cups of pellets do you feed daily? "))
        if size == "small" and pellets > 0.125:
            diet_plan.append(f"Cut back pellets from {pellets} cups to just 1/8 cup (2 tbsp) each day.")
        elif size == "medium" and pellets > 0.25:
            diet_plan.append(f"Reduce pellets from {pellets} cups to 1/4 cup daily.")
        elif (size == "large" or size == "giant") and pellets > 0.5:
            diet_plan.append(f"Cut pellets from {pellets} cups to 1/2 cup each day.")
    except ValueError:
        # error handling
        diet_plan.append("I need a real number for pellets.")
    return diet_plan


def check_greens_for_overweight(size):
    diet_plan = []
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
    return diet_plan


def check_treats_for_overweight():
    diet_plan = []
    try:
        treats = int(input("How many treats per day? "))
        if treats > 1:
            diet_plan.append(f"Too many treats! Cut from {treats} to just 1 small treat or none while slimming down.")
    except ValueError:
        diet_plan.append("Need a number for treats.")
    return diet_plan


def handle_underweight_bunny(size):
    diet_plan = []

    # check hay
    diet_plan.append("Keep hay available 24/7.")

    # check pellets
    diet_plan.extend(recommend_pellets_for_underweight(size))

    # Check greens
    diet_plan.extend(check_greens_for_underweight(size))

    # treats are more flexible
    diet_plan.extend(check_treats_for_underweight())

    # more reco.s for underweight bunnies
    diet_plan.append("Add some alfalfa hay - yes, even for adults.")
    diet_plan.append("Try a tiny bit of oats (1 tsp daily).")
    diet_plan.append("See the vet to check for health problems.")

    return diet_plan


def recommend_pellets_for_underweight(size):
    diet_plan = []
    if size == "small":
        diet_plan.append("More pellets - give 1/4 cup daily.")
    elif size == "medium":
        diet_plan.append("Bump up pellets to 1/3 cup daily.")
    else:  # large or giant
        diet_plan.append("Increase pellets to 3/4 cup daily.")
    return diet_plan


def check_greens_for_underweight(size):
    diet_plan = []
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
    return diet_plan


def check_treats_for_underweight():
    diet_plan = []
    try:
        treats = int(input("Treats per day? "))
        if treats < 2:
            diet_plan.append("Can offer up to 2 nutritious treats daily while gaining weight.")
    except ValueError:
        diet_plan.append("Need a number for treats.")
    return diet_plan


def handle_normal_weight_bunny(size):
    diet_plan = []

    # Maintain current good habits
    diet_plan.append("Current feeding looks good - keep it up.")

    # Recommend pellets
    diet_plan.extend(recommend_pellets_for_normal(size))

    # Adjust greens
    diet_plan.extend(check_greens_for_normal(size))

    # Keep treats moderate
    diet_plan.extend(check_treats_for_normal())

    # Always emphasize unlimited hay
    diet_plan.append("Keep unlimited hay available always.")

    return diet_plan


def recommend_pellets_for_normal(size):
    diet_plan = []
    if size == "small":
        diet_plan.append("Keep pellets at 1/8 cup (2 tbsp) daily.")
    elif size == "medium":
        diet_plan.append("Stay with 1/4 cup pellets daily.")
    else:  # large or giant
        diet_plan.append("Keep giving 1/2 cup pellets daily.")
    return diet_plan


def check_greens_for_normal(size):
    diet_plan = []
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
    return diet_plan


def check_treats_for_normal():
    diet_plan = []
    try:
        treats = int(input("Treats per day? "))
        if treats > 2:
            diet_plan.append(f"Too many treats! Go from {treats} down to 1-2 small treats daily.")
    except ValueError:
        diet_plan.append("Need a number for treats.")
    return diet_plan


def breedcheck():
    # examples of breeds and sizes
    size = input("Is your bunny small, medium, large, or giant sized? \nSmall: Netherland Dwarf, Jersey Wooly (1-5 lbs)\nMedium: Dutch, Dwarf Lop (6-9lbs)\nLarge: English Lop (9-11 lbs)\nGiant: Flemish Giant (11+ lbs)\n> ").lower()

    # error handling
    if size not in ["small", "medium", "large", "giant"]:
        print("That's not a valid size. Try again.")
        return breedcheck()  # Recursively try again

    # over, under, or normal weight
    weight_status = input("Is your bunny above weight, below weight, or average for their size? (above/below/average)\n> ").lower()

    # go to def function
    if weight_status == "above":
        diet_change(size, "overweight")
    elif weight_status == "below":
        diet_change(size, "underweight")
    else:
        diet_change(size, "normal")


def homepage():
    # first page
    print("CarrotCounter v1.0.0")
    print('By: Patrick Lee, Max Klochkov, Wesley Liu')
    print("DISCLAIMER: This is just for guidance. Always check with a vet before changing your bunny's diet")
    print("\n")
    print("Double check everything to be safe.")

    # Ask if user wants to start or exit
    if input("Ready to start? (y/n) ").lower() == "y":
        breedcheck()  # Begin the assessment process
    else:
        print("Thanks for using CarrotCounter!")


# Start the program when script is run directly
if __name__ == "__main__":
    homepage()
