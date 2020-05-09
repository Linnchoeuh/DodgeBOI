def language_detect():
    with open("custom_setting.txt", "r") as s:
        l= []
        l = s.readlines()
        alanguage = l[-1]
        alanguage = str(alanguage)
    if alanguage == "english":
        return 0
    elif alanguage == "french":
        return 1
    else:
        return -1

def loading_text(language = 0):
    if language == 0:
        return "Loading"
    if language == 1:
        return "Chargement"

def moving_mouse(language = 0):
    if language == 0:
        return "Move your mouse"
    if language == 1:
        return "Bougez votre souris"

def play_icon(language = 0):
    if language == 0:
        return "Play"
    if language == 1:
        return "Jouer"

def setting_icon(language = 0):
    if language == 0:
        return "Settings"
    if language == 1:
        return "Paramètres"

def score_icon(language = 0):
    if language == 0:
        return "Score"
    if language == 1:
        return "Score"

def quit(language = 0):
    if language == 0:
        return "Quit?"
    if language == 1:
        return "Quitter?"

def yes(language = 0):
    if language == 0:
        return "Yes"
    if language == 1:
        return "Oui"

def no(language = 0):
    if language == 0:
        return "No"
    if language == 1:
        return "Non"

def pause(language = 0):
    if language == 0:
        return "Pause"
    if language == 1:
        return "Pause"

def unpause(language = 0):
    if language == 0:
        return "Resume"
    if language == 1:
        return "Reprendre"

def back_to_menu(language = 0):
    if language == 0:
        return "Back to main-menu"
    if language == 1:
        return "Retourner au menu"

def Language(language = 0):
    if language == 0:
        return "Language:"
    if language == 1:
        return "Langue:"

def show_fps(language = 0):
    if language == 0:
        return "Show fps:"
    if language == 1:
        return "Afficher les fps:"

def text_aliasing(language = 0):
    if language == 0:
        return "Load text with aliasing:"
    if language == 1:
        return "Charger l'aliasing du texte:"

def resolution_modify(language = 0):
    if language == 0:
        return "Modify the screen resolution to:"
    if language == 1:
        return "Modifier la résolution d'affichage:"

def fullscreen(language = 0):
    if language == 0:
        return "Set fullscreen:"
    if language == 1:
        return "Mettre en plein écran:"

def framerate(language = 0):
    if language == 0:
        return "Set framelimit to:"
    if language == 1:
        return "Limiter les fps à:"

def apply(language = 0):
    if language == 0:
        return "Apply"
    if language == 1:
        return "Appliquer"

def lose(language = 0):
    if language == 0:
        return "You lose"
    if language == 1:
        return "Vous avez perdu"

def retry(language = 0):
    if language == 0:
        return "Retry"
    if language == 1:
        return "Réessayer"

def highscore(language = 0):
    if language == 0:
        return "Highscore"
    if language == 1:
        return "Highscore"

def controller_detected(language = 0):
    if language == 0:
        return "Controller detected!"
    if language == 1:
        return "Manette détectée!"

def connect_controller(language = 0):
    if language == 0:
        return "Connect controller"
    if language == 1:
        return "Connecter manette"

def disconnect_controller(language = 0):
    if language == 0:
        return "Disconnect controller"
    if language == 1:
        return "Déconnecter manette"

def searching_controller(language = 0):
    if language == 0:
        return "Searching controller..."
    if language == 1:
        return "Recherche manette..."

def tutorial(language = 0):
    if language == 0:
        return "Tutorial"
    if language == 1:
        return "Tutoriel"

def play(language = 0):
    if language == 0:
        return "Play"
    if language == 1:
        return "Jouer"

def tuto_help(language = 0):
    if language == 0:
        return "Click or press return to continue."
    if language == 1:
        return "Cliquez ou appuyez sur entrée pour continuer."

def tuto_rep1(language = 0):
    if language == 0:
        return "Hi, welcome to the DodgeBOI tutorial!"
    if language == 1:
        return "Bonjour et bienvenue dans le tutoriel de DodgeBOI!"

def tuto_rep2(language = 0):
    if language == 0:
        return "The purpose of this game is simple, dodge everything."
    if language == 1:
        return "Le but du jeu est simple, il faut tout esquiver."

def tuto_rep3(language = 0):
    if language == 0:
        return "For starting, you have to dodge these basic block"
    if language == 1:
        return "Pour commencer, esquivez ces quelques blocs basiques"

def tuto_rep3b(language = 0):
    if language == 0:
        return "use the directional pad or the left stick."
    if language == 1:
        return "utilisez la croix directionnel ou le stick gauche."

def tuto_rep3c(language = 0):
    if language == 0:
        return "with 'w' to up and 's' to down."
    if language == 1:
        return "avec 'z' pour monter et 's' pour descendre."

def tuto_rep4(language = 0):
    if language == 0:
        return "Execellent, then we can continue with the color wall,"
    if language == 1:
        return "Execellent, nous pouvons à présent continuer avec les murs colorés,"

def tuto_rep5(language = 0):
    if language == 0:
        return "you need to have the same color of bandana than the color of the wall incoming."
    if language == 1:
        return "vous avez besoin d'avoir la même couleur de bandana que le mur qui arrive."

def tuto_rep5b(language = 0):
    if language == 0:
        return "Use the button 'a'(blue),'b'(yellow),'x'(red) or x(blue),o(yellow),▲(red)."
    if language == 1:
        return "Utiliser les bouttons 'a'(bleu),'b'(jaune),'x'(rouge) or x(bleu),o(jaune),▲(rouge)."

def tuto_rep5c(language = 0):
    if language == 0:
        return "Use 'l'(red),'m'(blue),';'(yellow) or numpad1(red),2(blue),3(yellow)."
    if language == 1:
        return "Utilisez 'k'(rouge),'l'(bleu),'m'(jaune) ou 1(rouge),2(bleu) ou 3(jaune) du pad numérique."

def tuto_rep6(language = 0):
    if language == 0:
        return "Good, now I'll learn you how to slide."
    if language == 1:
        return "Bien, maintenant je vais vous aprendre à glisser."

def tuto_rep7(language = 0):
    if language == 0:
        return "When you're sliding, you can't move anymore."
    if language == 1:
        return "Quand vous glisser, vous ne pouvez pas bouger."

def tuto_rep7b(language = 0):
    if language == 0:
        return "To slide press l (controller)."
    if language == 1:
        return "Pour glisser appuyez sur l (manette)."

def tuto_rep7c(language = 0):
    if language == 0:
        return "To slide press 'q'."
    if language == 1:
        return "Pour glisser appuyez sur 'a'."

def tuto_rep8(language = 0):
    if language == 0:
        return "Great, now I'll learn you how to jump."
    if language == 1:
        return "Super, maintenant je vais vous aprendre à sauter."

def tuto_rep9(language = 0):
    if language == 0:
        return "Like the sliding, you can't move anymore.(you can't jump eternally)"
    if language == 1:
        return "Comme quand vous glisser,vous ne pouvez pas bouger.(vous ne pouvez pas sauter éternellement)"

def tuto_rep9b(language = 0):
    if language == 0:
        return "To jump press r (controller)."
    if language == 1:
        return "Pour sauter appuyez sur r (manette)."

def tuto_rep9c(language = 0):
    if language == 0:
        return "To jump press 'e'."
    if language == 1:
        return "Pour sauter appuyez sur 'e'."

def tuto_rep10(language = 0):
    if language == 0:
        return "Well, now I'll learn you how to kick."
    if language == 1:
        return "Génial, maintenant je vais vous aprendre à donner un coup de pied."

def tuto_rep11(language = 0):
    if language == 0:
        return "Like the sliding, you can't move anymore.(the kick is a quick action)"
    if language == 1:
        return "Comme quand vous glisser,vous ne pouvez pas bouger.(le coup de pied est une action courte)"

def tuto_rep11b(language = 0):
    if language == 0:
        return "To kick press y or ☐ (controller)."
    if language == 1:
        return "Pour donner un coup de pied appuyez sur y ou ☐ (manette)."

def tuto_rep11c(language = 0):
    if language == 0:
        return "To kick press 'space'."
    if language == 1:
        return "Pour donner un coup de pied appuyez sur 'espace'."

def text_finish(language = 0):
    if language == 0:
        return "You're finished the tutorial!"
    if language == 1:
        return "Vous avez fini le tutoriel!"