

class QuoteTerminalView:
    def show(self, quote):
        print(f'And the quote is: "{quote}"')

    def show2(self, quote):
        print(f'OTHER VIEW: Quote: "{quote}"')

    def error(self, msg):
        print(f'Error: {msg}')

    def select_quote(self):
        return input('Which quote number would you like to see? If you want to change a mode press 8. Press 9 to exit. ')
