"""Return a friendly greeting for a name."""


def greet(name: str) -> str:
    """Return Hello, <name>!; a blank name becomes world."""
    name = name.strip() or "world"
    return f"Hello, {name}!"
