"""Main dummy file for the project."""


class Main:
    """Main class for the project."""

    def __init__(self, colour: str):
        """Initialize the main class."""
        self.colour = colour
        self.colours = ["red", "green", "blue", "yellow", "pink", "purple"]

    def get_colour(self) -> str:
        """Get the colour of the main class."""
        if self.colour in self.colours:
            return f"The colour is {self.colour}."
        else:
            return "The colour is not in the list."

    def run(self):
        """Run the main logic of the project."""
        print(self.get_colour())


if __name__ == "__main__":
    main = Main("pink")
    main.run()
