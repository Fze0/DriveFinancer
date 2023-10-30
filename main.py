from gui import GUI
from taux_calculator import calcul_taux


def main():
    app = GUI()

    def calculate_taux():
        # Fonction pour calculer le taux d'emprunt en utilisant les valeurs sélectionnées
        values = app.get_selected_values()
        result, color = calcul_taux(*values)
        app.display_result(result, color)

    app.button_taux.configure(command=calculate_taux)

    app.app.mainloop()


if __name__ == '__main__':
    main()
