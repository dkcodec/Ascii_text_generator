import pyfiglet

def transfer (props, font):
    return pyfiglet.figlet_format(props, font=font)

def fonts():
    return pyfiglet.Figlet().getFonts()