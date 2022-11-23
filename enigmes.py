###IMPORTATIONS###
import random
import sys
import pickle
import time
import os.path
from utils import saut, mcmd
                
class Game:
    
    def __init__(self):
        self.command = commande(self)
        self.var_sauv = None
        self.argent = 0
        self.points = 0
        self.e_resol = 0
        self.e_ab = 0
        self.ct = 0
        self.espace = ' ' * 35
        self.e = 0
        self.nb_e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.indice_fournis = 0
        self.max_indices = 2
        self.améliorations = 0
        self.niv_ = 0
        self.essais_ = 0
        self.pt = 0
        self.ar_ = 0
        self.en = ["Si cela cache, ce n'est que pour mieux révéler.\nCela bloque autant que cela permet de passer.\nLa réponse est dans la question.\nQue suis-je ?",
     "Je suis le commencement de l’effroi,\nLa fin de la durée et de l’espace,\nLe commencement de toutes extrémités,\nEt la fin de chaque contrée.\nQui suis-je ?",
     "Celui qui le fabrique le vend,\nCelui qui l'achète ne s'en sert pas,\nCelui qui s'en sert ne le sais pas.\nQu'est-ce ?",
     "Je serai hier, j'étais demain.",
      "Je suis si fragile que lorsque l'on prononce mon nom, je meurs.",
      "Je suis tout au bout de ta main,\nJe commence la nuit et je finis demain.",
      "Je me vide en me remplissant,\nEt je me remplis en me vidant,\nQue suis-je?",
      "Les feignant me vénèrent, mais je suis leur pire énemie.\nLes travailleurs me craignent mais je pourrais les soulager.\nQue suis-je ?",
      "Plus j'ai de gardien, moins je suis en sécurité\nMoins j'ai de gardien, plus je suis en sécurité.\nQue suis-je ?",
      "Une boite sans charnière, sans clé, sans couvercle.\nPourtant à l'intérieur est caché un trésor doré.",
      "Lors d'une guerre, un chevalier fut transpercé, il en mourrut,\nun deuxiéme guerrier fut décapité et les deux écuiers eurent la tête tranchée.\nCombien y a-t-il eu de morts ?",
      "Lumières qui fuient la lumière.",
      "Vivant sans souffle,\nFroid comme la mort,\nJamais assoiffé, toujours buvant,\nEn cotte de mailles, jamais cliquetant.",
      "Sans pieds, Sans mains, Sans ailes,\nje monte au ciel.",
      "Tellement magique qu'il vient à vous tous les soirs,\nIl vous emmène partout sans vous déplacer.\nPour le voir, vous devez d'abord fermer les yeux."]
        self.repn = [("une enigme", "une énigme"),
            ("le e", " la lettre e", " le E"),
            "un cercueil",
            "aujourd'hui",
                "le silence",
                ("le n", "la lettre n", "le N"),
                "un sablier",
                "l'ennui",
                "un secret",
                "un oeuf",
                ("2", "deux"),
                ("les etoiles", "les étoiles"),
                "un poisson",
                ('une âme', 'une ame', 'la fumée', 'de la fumée'),
                ('le rêve', 'un rêve')]
        self.indices = ["Cette énigme est une énigme de niveau 3, par conséquent il n'y a pas d'indice disponible",
                "la réponse comporte 4 caractère, déterminant et espace compris",
                "c'est matériel",
                "c'est un moment",
                "c'est immatériel",
                "la réponse comporte 4 caractère, déterminant et espace compris",
                "Cette énigme est une énigme de niveau 3, par conséquent il n'y a pas d'indice disponible",
                "long de 5 caractère (déterminant et espace(s) eventuel(s) non compris), ça commence par un 'e'",
                "c'est immatériel",
                "ne pas prendre les mots au pied de la lettre",
                "faire attention aux sens de 'eurent'",
                "Cette énigme est une énigme de niveau 3, par conséquent il n'y a pas d'indice disponible",
                "le poid du son",
                "Cette énigme est une énigme de niveau 3, par conséquent il n'y a pas d'indice",
                ""]
                
        self.enigmes = {
            'e1' : self.en[0],
            'e2' :  self.en[1],
            'e3' :  self.en[2],
            'e4' : self.en[3],
            'e5' :  self.en[4],
            'e6' :  self.en[5],
            'e7' : self.en[6],
            'e8' : self.en[7],
            'e9' : self.en[8],
            'e10' : self.en[9],
            'e11' : self.en[10],
            'e12' : self.en[11],
            'e13' : self.en[12]
            }
        self.rep_enigme = {
            'rep e1' : self.repn[0],
            'rep e2' : self.repn[1],
            'rep e3' : self.repn[2],
            'rep e4' : self.repn[3],
            'rep e5' : self.repn[4],
            'rep e6' : self.repn[5],
            'rep e7' : self.repn[6],
            'rep e8' : self.repn[7],
            'rep e9' : self.repn[8],
            'rep e10' : self.repn[9],
            'rep e11' : self.repn[10],
            'rep e12' : self.repn[11],
            'rep e13' : self.repn[12]
            }
        self.idi = {
            'i 1' : self.indices[0],
            'i 2' : self.indices[1],
            'i 3' : self.indices[2],
            'i 4' : self.indices[3],
            'i 5' : self.indices[4],
            'i 6' : self.indices[5],
            'i 7' : self.indices[6],
            'i 8' : self.indices[7],
            'i 9' : self.indices[8],
            'i 10' : self.indices[9],
            'i 11' : self.indices[10],
            'i 12' : self.indices[11],
            'i 13' : self.indices[12]
            }
    def sauver(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):
        self.var_sauv = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]
        fich_sauv = open("fich_sauv", "wb")
        pickle.dump(self.var_sauv, fich_sauv)
        fich_sauv.close()
    
    def charger(self):
        fichier = "fich_sauv"
        if os.path.isfile(fichier):
            fich_sauv = open(fichier, 'rb')
            var_sauv = pickle.load(fich_sauv)
            fich_sauv.close()
            self.argent = var_sauv[0]
            self.points = var_sauv[1]
            self.e_resol = var_sauv[2]
            self.e_ab = var_sauv[3]
            self.ct = var_sauv[4]
            self.espace = var_sauv[5]
            self.e = var_sauv[6]
            self.nb_e = var_sauv[7]
            self.indice_fournis = var_sauv[8]
            self.max_indices = var_sauv[9]
            self.améliorations = var_sauv[10]
            self.niv_ = var_sauv[11]
            self.essais_ = var_sauv[12]
            self.pt = var_sauv[13]
            self.ar_ = var_sauv[14]
        else:
            print("Le fichier de sauvegarde '%s' n'existe pas" % fichier)
    
    def tirer_enigme(self):
        
        if len(self.nb_e) == 0:
            saut()
            saut()
            print("BRAVO A VOUS !!!! VOUS AVEZ RESOLU TOUTES LES ENIGMES, VOUS AVEZ FINI LE JEU !!!!")
            print("/reset pour recommencer une partie en réinitialisant toutes les données. Sinon /leave")
            print("pour quitter définitivement")
            saut()
            choice = input()
            if choice == '/leave':
                sys.exit()
            elif choice == '/reset':
                self.reset()
            elif choice not in ('/reset', '/leave'):
                mcmd()
                self.tirer_enigme()
        else:
            self.e = random.choice(self.nb_e)
            saut()
            print("...")
            saut()
            print("Tirage de l'enigme en cours...")
            saut()
            print("...")
            saut()
            print(self.enigmes['e%s' % self.e])
            self.nb_e.remove(self.e)
            if self.e in (2, 4, 6, 9, 11):
                self.niv_ = 1
                self.essais_ = 3
                self.pt_ = 1
                self.ar_ = random.randint(6, 18)
                self.sauver(self.argent, self.points, self.e_resol, self.e_ab, self.ct, self.espace, self.e, self.nb_e, self.indice_fournis, self.max_indices, self.améliorations, self.niv_, self.essais_, self.pt, self.ar_)
                self.repondre()
            elif self.e in (3, 5, 8, 10, 13):
                self.niv_ = 2
                self.essais_ = 2
                self.pt_ = 2
                self.ar_ = random.randint(18, 30)
                self.sauver(self.argent, self.points, self.e_resol, self.e_ab, self.ct, self.espace, self.e, self.nb_e, self.indice_fournis, self.max_indices, self.améliorations, self.niv_, self.essais_, self.pt, self.ar_)
                self.repondre()
            elif self.e in (1, 7, 12, 14):
                self.niv_ = 3
                self.essais_ = 2
                self.pt_ = 3
                self.ar_ = random.randint(30, 42)
                self.sauver(self.argent, self.points, self.e_resol, self.e_ab, self.ct, self.espace, self.e, self.nb_e, self.indice_fournis, self.max_indices, self.améliorations, self.niv_, self.essais_, self.pt, self.ar_)
                self.repondre()
    
    def repondre(self):
        
        rep = input()
        if rep in self.rep_enigme['rep e%s' % self.e] or rep == 'triche':
            saut()
            print("Bonne réponse !!!!")
            self.ct = 0
            self.points = self.points + self.pt
            self.argent += self.ar_
            self.e_resol = self.e_resol + 1
            print("+ %s point !!" % self.pt)
            print("+ %s$ !!" % self.ar_)
            self.sauver(self.argent, self.points, self.e_resol, self.e_ab, self.ct, self.espace, self.e, self.nb_e, self.indice_fournis, self.max_indices, self.améliorations, self.niv_, self.essais_, self.pt, self.ar_)
            help(self)
        elif rep == '/abandon':
            saut()
            self.e_ab = self.e_ab + 1
            print("Très bien...")
            saut()
            print("points : %s" % self.points)
            self.nb_e.append(self.e)
            self.sauver(self.argent, self.points, self.e_resol, self.e_ab, self.ct, self.espace, self.e, self.nb_e, self.indice_fournis, self.max_indices, self.améliorations, self.niv_, self.essais_, self.pt, self.ar_)
            help(self)
        elif rep == '/indice':
            if self.indice_fournis in (0, 1):
                saut()
                print(self.idi['i %s' % self.e])
                if self.idi['i %s' % self.e] == "Cette énigme est une énigme de niveau %s, par conséquent il n'y a pas d'indice disponible" % self.niv_:
                    pass
                else:
                    self.indice_fournis += 1
            elif self.indice_fournis == self.max_indices:
                saut()
                print("Vous avez déjà eu tous vos indices !!")
            self.repondre()
        elif rep == '/niveau':
            saut()
            print("enigme de niveau %s" % self.niv_)
            self.repondre()
        elif '/' in rep:
            mcmd()
            self.repondre()
        else:
            while rep != self.rep_enigme['rep e%s' % self.e]:
                ct = ct + 1
                saut()
                print("Mauvaise réponse !")
                saut()
                rep = input()
                if rep in self.rep_enigme['rep e%s' % self.e]:
                    saut()
                    print("Bonne réponse !!!!")
                    if self.ct > self.essais_:
                        print("%s réponses ou plus ont été écrites donc vous ne gagnez pas de points à cette énigme-ci..." % self.essais_)
                        help(self)
                    else:
                        self.points = self.points + self.pt
                        self.argent += self.ar_
                    self.e_resol = self.e_resol + 1
                    self.ct = 0
                    print("+ %s point !!" % self.pt)
                    print("+ %s$ !!" % self.ar_)
                    self.sauver(self.argent, self.points, self.e_resol, self.e_ab, self.ct, self.espace, self.e, self.nb_e, self.indice_fournis, self.max_indices, self.améliorations, self.niv_, self.essais_, self.pt, self.ar_)
                    help(self)
                elif rep == '/abandon':
                    saut()
                    self.e_ab = self.e_ab + 1
                    self.ct = 0
                    print("Très bien...")
                    saut()
                    print("points : %s" % self.points)
                    self.sauver(self.argent, self.points, self.e_resol, self.e_ab, self.ct, self.espace, self.e, self.nb_e, self.indice_fournis, self.max_indices, self.améliorations, self.niv_, self.essais_, self.pt, self.ar_)
                    help(self)
                elif rep == '/indice':
                    if self.indice_fournis in (0, 1):
                        saut()
                        print(self.idi['i %s' % self.e])
                        if self.idi['i %s' % self.e] == "Cette énigme est une énigme de niveau %s, par conséquent il n'y a pas d'indice disponible" % self.niv_:
                            pass
                        else:
                            self.indice_fournis += 1
                    elif self.indice_fournis == self.max_indices:
                        saut()
                        print("Vous avez déjà eu tous vos indices !!")
                    self.repondre()
                elif rep == '/niveau':
                    saut()
                    print("enigme de niveau %s" % self.niv_)
                    self.repondre()
                elif '/' in rep:
                    mcmd()
                    self.repondre()

class commande:
    
    game: Game
    def  __init__(self, game : Game):
        self.game = game 
    
    def help(self):
        saut()
        cmd = input("Tapez /help pour connaitre toutes les commande de jeu.\n(Vous pouvez taper directement la commande voulue au lieu\nde passer par /help si vous connaissez la commande souhaitée) : ")
        if cmd == '/help':
            saut()
            print("/enigme : tirer une énigme au hasard\n/stat : voir ses statistiques\n/leave : quitter la partie(attention, si vous quitter, rien ne sera enregistré !)\n/rules : voir les règles du jeu\n/shop : acéder au magasin")
            print("/reset : réinitialiser le jeu")
            help(game)
        elif cmd == '/stat':
            self.game.commande.info()
        elif cmd == '/leave':
            self.game.commande.leave()
        elif cmd == '/enigme':
            self.game.tirer_enigme()
        elif cmd == '/rules':
            self.game.commande.rules()
        elif cmd == '/config':
            self.game.commande.config_niveau()
        elif cmd == '/shop':
            self.game.commande.shop()
        elif cmd == '/reset':
            self.game.commande.reset()
        else:
            cm = False
            while cm == False:
                mcmd()
                cmd = input()
                if cmd == '/help':
                    saut()
                    print("/enigme : tirer une énigme au hasard\n/stat : voir ses statistiques\n/leave : quitter la partie(attention, si vous quitter, rien ne sera enregistré !)\n/rules : voir les règles du jeu")
                    cm = True
                    help(game)
                if cmd == '/stat':
                    cm = True
                    self.game.commande.info()
                elif cmd == '/leave':
                    cm = True
                    self.game.commande.leave()
                elif cmd == '/enigme':
                    cm = True
                    self.game.tirer_enigme()
                elif cmd == '/rules':
                    cm = True
                    self.game.commande.rules()
                elif cmd == '/config':
                    cm = True
                    self.game.commande.config_niveau()
                elif cmd == '/shop':
                    cm = True
                    self.game.commande.shop()
                elif cmd == '/reset':
                    cm = True
                    self.game.commande.reset()
                            
    def info(self):
        saut()
        if self.game.points >= 10 and self.game.points < 20:
            self.game.améliorations += 1
            if self.game.améliorations == 1:
                print("BRAVO !! Vous avez atteint les 10 points ou plus !\nVous débloquez 1 indice suplémentaire !!")
                self.game.max_indices += 1
        elif self.game.points >= 20:
            self.game.améliorations += 1

            if self.game.améliorations == 2:
                print("BRAVO !! Vous avez atteint les 20 points ou plus !\nVous débloquez 2 indice suplémentaire !!")
                self.game.max_indices += 2
            elif self.game.améliorations == 1:
                print("BRAVO !! Vous avez atteint les 10 points ou plus !\nVous débloquez 1 indice suplémentaire !!")
                self.game.max_indices += 1
                saut()
                self.game.améliorations += 1
                print("BRAVO !! Vous avez atteint les 20 points ou plus !\nVous débloquez 2 indice suplémentaire !!")
                self.game.max_indices += 2
        print("Vos statistiques :\n\npoints : %s\nnb d'énigme résolues : %s\nenigmes abandonnées : %s\nvotre argent : %s$\nindices disponibles : %s\nindices utilisés : %s" % (points, e_resol, e_ab, argent, (max_indices - indice_fournis), indice_fournis))
        saut()
        self.game.sauver(self.game.argent, self.game.points, self.game.e_resol, self.game.e_ab, self.game.ct, self.game.espace, self.game.e, self.game.nb_e, self.game.indice_fournis, self.game.max_indices, self.game.améliorations, self.game.niv_, self.game.essais_, self.game.pt, self.game.ar_)
        help(game)
    def leave(self):
        saut()
        sur = input("Êtes-vous sur (oui/non) ? ")
        if sur == 'oui':
            saut()
            print("Très bien...")
            sys.exit()
        elif sur == 'non':
            saut()
            print("Ok")
            help(self)
        else:
            mcmd()
            self.leave()
    def rules(self):
        saut()
        rules = open("enigme/rules.txt", encoding="utf8")
        R = rules.read()
        print(R)
        saut()
        p = input("vous pouvez faire /config ou 'pass' pour retrouner à l'accueil : ")
        if p == '/config':
            self.config_niveau()
        elif p == 'pass' or "'pass'":
            saut()
            print("Très bien...")
            help(self)
        else:
            while p != '/config' or 'pass' or "'pass'":
                mcmd()
                p = input("vous pouvez faire /config ou 'pass' pour retrouner à l'accueil : ")
                if p == '/config':
                    self.config_niveau()
                elif p == 'pass' or "'pass'":
                    help(game)
    def config_niveau(self):
        saut()
        print("Caractérisiques des niveaux : \n\nniveau 1 : 1 indice possible\n           3 essais avant l'anulation du comptage des points de l'enigme\n           rapporte 1 point\n           rapporte entre 6 et 18$\nniveau 2 : 1 indice possible\n           2 essais possibles avant l'anunulation du comptage des points\n           rapporte 2 points\n           rapporte entre 18 et 30$\nniveau 3 : aucun indices possibles\n           2 essais avant l'anulation du comptage des points\n           rapporte 3 points\n           rapporte entre 30 et 42$.")
        help(game)

    def shop(self):
        saut()
        SHOP = open("enigme/shop.txt", encoding="utf8")
        shop = SHOP.read()
        print(shop)
        saut()
        print("argent : %s" % self.game.argent)
        saut()
        print("Tapez ici le numéro de l'article que vous voulez acheter, sinon 'pass' pour fermer le shop :")
        choix = input()
        if choix in ('pass', "'pass'"):
            saut()
            print("Très bien ")
            print("Revenez vite !")
            saut()
            help(game)
        elif choix in ("1", "1)"):
            if self.game.argent >= 70:
                saut()
                self.game.max_indices += 1
                self.game.argent -= 70
                print("Super !")
                print("Merci, revenez vite !")
                saut()
                print("argent : %s" % self.game.argent)
                saut()
                self.game.sauver(self.game.argent, self.game.points, self.game.e_resol, self.game.e_ab, self.game.ct, self.game.espace, self.game.e, self.game.nb_e, self.game.indice_fournis, self.game.max_indices, self.game.améliorations, self.game.niv_, self.game.essais_, self.game.pt, self.game.ar_)
                help(game)
            else:
                saut()
                print("Vous n'avez pas assez d'argent :(")
                help(game)
        elif choix in ("2", "2)"):
            if self.game.argent >= 135:
                saut()
                self.game.max_indices += 2
                self.game.argent -= 135
                print("Super !")
                print("Merci, revenez vite !")
                saut()
                print("argent : %s" % self.game.argent)
                saut()
                self.game.sauver(self.game.argent, self.game.points, self.game.e_resol, self.game.e_ab, self.game.ct, self.game.espace, self.game.e, self.game.nb_e, self.game.indice_fournis, self.game.max_indices, self.game.améliorations, self.game.niv_, self.game.essais_, self.game.pt, self.game.ar_)
                help(game)
            else:
                saut()
                print("Vous n'avez pas assez d'argent :(")
                help()
        elif choix in ('3', '3)'):
            if self.game.argent >= 195:
                saut()
                self.game.max_indices += 3
                self.game.argent -= 195
                print("Super !")
                print("Merci, revenez vite !")
                saut()
                print("argent : %s" % self.game.argent)
                saut()
                self.game.sauver(self.game.argent, self.game.points, self.game.e_resol, self.game.e_ab, self.game.ct, self.game.espace, self.game.e, self.game.nb_e, self.game.indice_fournis, self.game.max_indices, self.game.améliorations, self.game.niv_, self.game.essais_, self.game.pt, self.game.ar_)
                help(game)
            else:
                saut()
                print("Vous n'avez pas assez d'argent :(")
                help(game)
        elif choix in ('4', '4)'):
            if self.game.argent >= 50:
                saut()
                print("Alors...")
                saut()
                print("...")
                saut()
                print("Vous n'avez pas le droit à un indice et vous n'avez qu'un essais !!")
                saut()
                print("Quelle est la couleur du cheval blanc d'henri IV ??")
                rep = input()
                if rep == 'blanc':
                    saut()
                    print("BRAVO !!! C'était difficile non ?")
                    argent_argent = random.randint(10, 20) * 3
                    saut()
                    print("+ %s$ !" % argent_argent)
                    print("+ 6 points !")
                    self.game.argent += argent_argent
                    self.game.points += 6
                    self.game.sauver(self.game.argent, self.game.points, self.game.e_resol, self.game.e_ab, self.game.ct, self.game.espace, self.game.e, self.game.nb_e, self.game.indice_fournis, self.game.max_indices, self.game.améliorations, self.game.niv_, self.game.essais_, self.game.pt, self.game.ar_)
                    help(game)
                else:
                    saut()
                    print("raté ! c'était facile pourtant !")
                    help(game)
            else:
                saut()
                print("Vous n'avez pas assez d'argent :(")
                help(game)
        elif choix in ('5', '5)'):
            if self.game.argent >= 30:
                saut()
                print("Voulez-vous vraiment savoir l'information ultra-confidentielle?")
                saut()
                print("En fait comme vous avez deja payé je vais la dire... :)")
                saut()
                saut()
                print("LES CHAUSSETTES DE L'ARCHIDUCHESSE SONT SECHES !! PAS ARCHISECHES !!!!")
                help(game)
            else:
                saut()
                print("Vous n'avez pas assez d'argent :(")
                help(game)
        else:
            mcmd()
            self.shop()
    def reset(self):
        self.game.argent = 0
        self.game.points = 0
        self.game.e_resol = 0
        self.game.e_ab = 0
        self.game.ct = 0
        self.game.e = 0
        self.game.indice_fournis = 0
        self.game.améliorations = 0
        self.game.niv_ = 0
        self.game.essais_ = 0
        self.game.pt_ = 0
        self.game.ar_ = 0
        self.game.nb_e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.game.max_indices = 2
        saut()
        saut()
        time.sleep(1)
        str = "Réinitialisation terminée !!"
        x = str.center(153, "-")
        print(x)
        saut()
        saut()
        self.game.sauver(self.game.argent, self.game.points, self.game.e_resol, self.game.e_ab, self.game.ct, self.game.espace, self.game.e, self.game.nb_e, self.game.indice_fournis, self.game.max_indices, self.game.améliorations, self.game.niv_, self.game.essais_, self.game.pt, self.game.ar_)
        help(game)

###BOUCLE PRINIPALE###

game = Game()
print()
print()
s = "BIENVENUE DANS UN JEU D'ENIGMES !!!"
xx = s.center(153, '=')
print(xx)
saut()
game.charger()
saut()
help(game)
