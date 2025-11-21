from spellchecker import SpellChecker


class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_list = []

        for word in words:
            corrected = self.spell.correction(word)

            # fix NoneType by keeping original word
            if corrected is None:
                corrected = word

            # show correction only when changed
            if corrected != word:
                print(f"Correcting {word} to {corrected}")

            corrected_list.append(str(corrected))

        return " ".join(corrected_list)

    def run(self):
        print("\n__Spell Checker__\n")
        while True:
            text = input("Enter text to check (or type exit to quit): ")

            if text.lower() == "exit":
                print("Closing the program...")
                break

            corrected_text = self.correct_text(text)
            print(f"Corrected Text: {corrected_text}")


if __name__ == "__main__":
    SpellCheckerApp().run()
