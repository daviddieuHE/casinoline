class player:

    profile = {}

    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def wallet(self):
        return self.__wallet
    @wallet.setter
    def wallet(self, wallet):
        self.__wallet = wallet

    def __init__(self, surname, wallet):
        self.__surname = surname
        self.__surname = wallet

    def creatPlayer():
        """
        fonction qui sert à créer le profil du joueur en lui demandant son surnom ainsi que la valeur de son wallet
        :return: none
        """
        player.profile[0]=player((input("Quel est votre surnom ?")), int((input("Quelle est la valeur de votre wallet ?"))))

