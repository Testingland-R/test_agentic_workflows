"""colour_validator.py - Colour Validator for checking valid colours."""


class ColourValidator:
    """Colour validator for checking valid colours."""

    def __init__(self, colour: str):
        """Initialize the colour validator."""
        self.colour = colour
        self.colours = ["red", "green", "blue", "yellow", "pink", "purple"]

    def get_colour(self) -> str:
        """Get the colour of the colour validator."""
        if self.colour in self.colours:
            return f"The colour is {self.colour}."
        else:
            return "The colour is not in the list."

    def run(self):
        """Run the main logic of the project."""
        print(self.get_colour())
