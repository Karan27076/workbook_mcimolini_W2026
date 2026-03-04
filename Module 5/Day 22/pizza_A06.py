def make_pizza(size, crust):
    """Summarize the pizza we are about to make:"""
    print("\nMaking a " + str(size) + " - inch pizza with " + crust +" crust.")

def make_pizza_with_default(size=12, crust="thin"):
    """Summarize the pizza we are about to make:"""
    print("\nMaking a " + str(size) + " - inch pizza with " + crust +" crust.")

if __name__ == "__main__":
    make_pizza(16, "thin")
    make_pizza(12, "thick")
    make_pizza(crust= "medium", size = 18)


    make_pizza_with_default()
    make_pizza_with_default(22)
    make_pizza_with_default("thin")  
    make_pizza_with_default(crust="medium")