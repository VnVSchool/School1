class Toyota:
    def __init__(self, engine):
        self.__engine = engine

    def drive(self):
        print("driving")

    def engine_info(self):
        print(self.__engine)


class Camry(Toyota):

    def drive(self):
        print("Camry driving")
    def turn_on_eco(self):
        print("Eco turned on")


toyota = Toyota(2.0)
toyota.drive()
toyota.engine_info()

camry3 = Camry(3.5)
camry3.drive()
camry3.engine_info()
camry3.turn_on_eco()
