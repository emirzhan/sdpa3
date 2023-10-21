# Interfaces
class OldSystem:
    def perform_action(self):
        pass

class NewSystem:
    def take_action(self):
        pass

# Class
class LegacySystem(OldSystem):
    def perform_action(self):
        print("Legacy System is performing the action.")

class ModernSystem(NewSystem):
    def take_action(self):
        print("Modern System is taking the action.")


class Adapter(OldSystem):
    def __init__(self, new_system):
        self.new_system = new_system

    def perform_action(self):
        self.new_system.take_action()

if __name__ == "__main__":
    modern_system = ModernSystem()
    adapter = Adapter(modern_system)
    legacy_system = LegacySystem()

    legacy_system.perform_action()
    adapter.perform_action()
