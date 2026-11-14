class MainModel:
    def generate_greeting(self, name):
        if not name.strip():
            return "Please enter a name."

        return f"Hello, {name}!"