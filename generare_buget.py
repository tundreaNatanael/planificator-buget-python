from cvs_handler import CVS
import csv
class EventBudget:
    # Constants
    chirie_fixa = 15000

    chirie_per_two_pers_low_end = 100
    chirie_per_two_pers_high_end = 200

    mas_per_pers_low_end = 50
    mas_per_pers_high_end = 100

    pret_excursie_per_pers_low_end = 100
    pret_excursie_per_pers_high_end = 200

    kit_invitati_low_end = 500
    kit_invitati_high_end = 1000

    def __init__(self, data):
        # print("Received data object:", data)
        data_dict = {item['categorie']: item['optiune'] for item in data}
        self.nr_zile = int(data_dict.get('nr_zile', 0))
        self.nr_participanti = int(data_dict.get('nr_participanti', 0))
        self.nr_invitati = int(data_dict.get('nr_invitati', 0))
        self.tip_eveniment = data_dict.get('tip_eveniment', '')
        self.early_bird = bool(int(data_dict.get('early_bird', 0)))
        self.activitati_extra = data_dict.get('activitati_extra', '').split('/') if data_dict.get('activitati_extra', '') else []
        self.voluntari = int(data_dict.get('voluntari', 0))
        self.contractori_externi = data_dict.get('contractori_externi', '')
    def print_variables(self):
        print(f"nr_zile: {self.nr_zile}")
        print(f"nr_participanti: {self.nr_participanti}")
        print(f"nr_invitati: {self.nr_invitati}")
        print(f"tip_eveniment: {self.tip_eveniment}")
        print(f"early_bird: {self.early_bird}")
        print(f"activitati_extra: {self.activitati_extra}")
        print(f"voluntari: {self.voluntari}")
        print(f"contractori_externi: {self.contractori_externi}")
    def calculeaza_buget(self):
        nr_zile = self.nr_zile

        nr_participanti = self.nr_participanti
        nr_invitati = self.nr_invitati
        voluntari = self.voluntari

        total_pers = nr_participanti + nr_invitati + voluntari

        chirie_fixa = self.chirie_fixa
        chirie_per_two_pers = self.chirie_per_two_pers_low_end if self.tip_eveniment == 'low_end' else self.chirie_per_two_pers_high_end
        mas_per_pers = self.mas_per_pers_low_end if self.tip_eveniment == 'low_end' else self.mas_per_pers_high_end
        
        pret_excursie_per_pers = self.pret_excursie_per_pers_low_end if self.tip_eveniment == 'low_end' else self.pret_excursie_per_pers_high_end
        kit_invitati = self.kit_invitati_low_end if self.tip_eveniment == 'low_end' else self.kit_invitati_high_end


        cazare = (chirie_fixa + ((total_pers * chirie_per_two_pers) // 2)) * nr_zile
        mancare = total_pers * mas_per_pers * nr_zile
        excursie = total_pers * pret_excursie_per_pers
        kituri = nr_invitati * kit_invitati
        total = cazare + mancare + excursie + kituri
        print("total:   " f"{total:.2f} lei")

        # Prepare data to write
        results = [
            {"categorie": "cazare", "valoare": f"{cazare:.2f}"},
            {"categorie": "mancare", "valoare": f"{mancare:.2f}"},
            {"categorie": "excursie", "valoare": f"{excursie:.2f}"},
            {"categorie": "kituri", "valoare": f"{kituri:.2f}"},
            {"categorie": "Total", "valoare": f"{total:.2f}"},
        ]

        CVS.write_buget(results)