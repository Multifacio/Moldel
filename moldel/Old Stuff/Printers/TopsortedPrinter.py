from Printers.Printer import Printer

class TopsortedPrinter(Printer):
    """ The Topsorted Printer is the most basic printer that print the likelihoods of the candidates that they are
        the Mol. This is sorted from the highest likelihood to the least likelihood """

    def do_print(self, res):
        sort_res = list()
        for key, value in res.items():
            sort_res.append((key.value.name, value))
        sort_res.sort(key=lambda x: x[1], reverse=True)
        for row in sort_res:
            name = row[0]
            prob = row[1]
            print(name + ": " + str(prob))