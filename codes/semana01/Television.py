# --------------------------------------------------
# Definindo classe Televisão
# --------------------------------------------------

class Television:

    # construtor
    def __init__(self):
        self.__powerOn = False
        self.__muted = False
        self.__volume = 5
        self.__channel = 2
        self.__prevChannel = 2

    def togglePower(self):
        self.__powerOn = not self.__powerOn
    
    def toggleMute(self):
        if self.__powerOn:
            self.__muted = not self.__muted
    
    def volumeUp(self):
        if self.__powerOn:
            if self.__volume <10:
                self.__volume +=1
            self.__muted = False
            return self.__volume
    
    def channelUp(self):
        if self.__powerOn:
            self.__prevChannel = self.__channel
            if self.__channel == 99:
                self.__channel = 2
            else:
                self.__channel +=1
            return self.__channel
        
    def setChannel(self, number):
        if self.__powerOn:
            if 2 <= number <= 99:
                self.__prevChannel = self.__channel
                self.__channel = number 
            return self.__channel
    
    def jumpPrevChannel(self):
        if self.__powerOn:
            incoming = self.__channel
            self.__channel = self.__prevChannel 
            self.__prevChannel = incoming
            return self.__channel
    
    def __str__(self):
        display = 'Power setting is currently ' + str(self.__powerOn) +'\n'
        display += 'Channel setting is currently ' + str(self.__channel) +'\n'
        display += 'Volume setting is currently ' + str(self.__volume) +'\n'
        display += 'Mute is currently ' + str(self.__muted)
        return display

# --------------------------------------------------
# Função principal
# --------------------------------------------------
if __name__ == "__main__":
    tv = Television()
    print(type(tv))
    print(tv)

# --------------------------------------------------
