from Printers.Printer import Printer
import matplotlib.pyplot as plt

class PiechartPrinter(Printer):
    """ The Pie Chart Printer prints a pie chart with the likelihoods that players are the Mol """

    def do_print(self, res):
        labels = list()
        sizes = list()
        for key, value in res.items():
            if value != 0.0:
                labels.append(key.value.name)
                sizes.append(value)
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()