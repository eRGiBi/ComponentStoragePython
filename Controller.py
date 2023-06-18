from File.Loader import Loader
from Model.GloveParser import GloveParser
from Model.GloveStorage import GloveStorage


class Controller:

    file_name = "Data.csv"

    def __init__(self):
        self.costumers = []

    def start(self):

        gst = GloveStorage()
        parser = GloveParser(self.costumers)
        loader = Loader()
        gst.add(loader.load(Controller.file_name, parser))

        print(gst)

        gst.sort_by_quantity()

        print(gst)