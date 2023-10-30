import customtkinter
from PIL import Image


class GUI:
    def __init__(self):
        # Initialisation de l'interface graphique
        customtkinter.set_appearance_mode("Light")
        customtkinter.set_default_color_theme("green")
        self.app = customtkinter.CTk()
        self.app.geometry("500x500")
        self.app.iconbitmap("image/logo.ico")
        self.app.title("Green Bank")
        self.frame = customtkinter.CTkFrame(master=self.app)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Création du label de titre
        self.titre = customtkinter.CTkLabel(master=self.frame, justify=customtkinter.LEFT,
                                            text="Simulateur d’emprunt pour l'achat d’une voiture")
        self.titre.configure(font=("Arial", 14, "bold"), text_color="green")
        self.titre.pack(pady=10, padx=10)

        # Création des menus déroulants
        self.menu_type = customtkinter.CTkOptionMenu(master=self.frame,
                                                     values=["Citadine", "Cabriolet", "Berline", "SUV / 4x4"])
        self.menu_type.pack(pady=10, padx=10)
        self.menu_type.set("Type de véhicule")

        self.menu_energie = customtkinter.CTkOptionMenu(master=self.frame,
                                                        values=["Essence", "Electrique", "Gaz", "Diesel", "Hybride"])
        self.menu_energie.pack(pady=10, padx=10)
        self.menu_energie.set("Energie")

        self.menu_km = customtkinter.CTkOptionMenu(master=self.frame,
                                                   values=["5k-10k/km", "10k-15k/km", "15k-20k/km", "20k-25k/km",
                                                           "25k-30k/km"])
        self.menu_km.pack(pady=10, padx=10)
        self.menu_km.set("Kilometrage")

        self.menu_annee = customtkinter.CTkOptionMenu(master=self.frame,
                                                      values=["1960-1970", "1970-1980", "1980-1990", "1990-2000",
                                                              "2000-2010", "Après 2010"])
        self.menu_annee.pack(pady=10, padx=10)
        self.menu_annee.set("Année")

        self.menu_passagers = customtkinter.CTkOptionMenu(master=self.frame, values=["1", "2", "3", "4"])
        self.menu_passagers.pack(pady=10, padx=10)
        self.menu_passagers.set("Passagers")

        # Création du bouton de calcul
        self.button_taux = customtkinter.CTkButton(master=self.frame, command=None, text="Calcul taux")
        self.button_taux.pack(pady=10, padx=10)

        # Création de l'affichage des résultats
        self.resultat = customtkinter.CTkLabel(self.frame, text="Veuillez insérer tous les éléments")
        self.resultat.pack(pady=10, padx=10)

        # Désactivation du redimensionnement de la fenêtre
        self.app.resizable(width=False, height=False)

    def get_selected_values(self):
        # Récupération des valeurs sélectionnées dans les menus déroulants
        type_vehicule = self.menu_type.get()
        energie = self.menu_energie.get()
        km_par_an = self.menu_km.get()
        annee_fabrication = self.menu_annee.get()
        nb_personnes = self.menu_passagers.get()
        return type_vehicule, energie, km_par_an, annee_fabrication, nb_personnes

    def display_result(self, result, color):
        # Affichage du résultat
        self.resultat.configure(text=result, text_color=color)