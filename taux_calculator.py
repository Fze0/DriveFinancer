from data import TYPE_SCORES, ENERGIE_SCORES, KM_SCORES, ANNEE_SCORES, PASSENGER_SCORES


def calcul_taux(type_vehicule, energie, km_par_an, annee_fabrication, nb_personnes):
    # Calcul du taux d'emprunt en fonction des critères
    criteria_scores = {
        "Type de véhicule": TYPE_SCORES.get(type_vehicule, 0),
        "Type d'énergie": ENERGIE_SCORES.get(energie, 0),
        "Nombre de kilomètres par an": KM_SCORES.get(km_par_an, 0),
        "Année de fabrication": ANNEE_SCORES.get(annee_fabrication, 0),
        "Nombre de passagers": PASSENGER_SCORES.get(nb_personnes, 0)
    }

    error_messages = []
    for criterion, score in criteria_scores.items():
        if score == 0:
            error_messages.append(criterion + " invalide")
    if error_messages:
        error_message = "Veuillez corriger les erreurs suivantes:\n- " + "\n- ".join(error_messages)
        return error_message, "red"

    # Calcul du score total et du taux d'emprunt
    scores = sum(criteria_scores.values())
    taux_emprunt = (
        3 if 0 <= round(scores) <= 10 else
        2.74 if 11 <= round(scores) <= 15 else
        2.52 if 16 <= round(scores) <= 25 else
        2.1 if 26 <= round(scores) <= 33 else
        1.85 if 34 <= round(scores) <= 40 else
        None)
    if taux_emprunt is not None:
        taux_emprunt += criteria_scores["Nombre de passagers"]
        return "Le taux d'emprunt est de {:.2f} %".format(taux_emprunt), "black"
    else:
        return "Taux non calculé", "red"