from MVC.QuoteModel import QuoteModel
from MVC.QuoteTerminalView import QuoteTerminalView


class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()
        self.view_mode = 0

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                if n == 8:
                    if self.view_mode == 0:
                        self.view_mode = 1
                    elif self.view_mode == 1:
                        self.view_mode = 0
                    print("Your view mode was changed! ")
                if n == 9:
                    exit()
                else:
                    valid_input = True
            except ValueError as err:
                self.view.error(f"Incorrect index '{n}'")
        quote = self.model.get_quote(n)
        if n != 8:
            if self.view_mode == 0:
                self.view.show(quote)
            elif self.view_mode == 1:
                self.view.show2(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == '__main__':
    main()
