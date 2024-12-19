def waste(waste_types):
    waste_categories = {
        'plastmasas pudele':'Plastmasas',
        'alumīnija kanniņa':'Metāla',
        'piena kartons':'Papīra',
        'augļi':'Organisko atkritumu',
        'stikla pudele':'Stikla',
        'dators':'E-atkritumu',
        'banāna miza':'Organisko atkritumu',
        'kartons':'Papīra',
        'plastmasas maisiņš':'Plastmasas',
        'koku lapas':'Organisko atkritumu'
    }

    waste_types = waste_types.lower().strip()

    if waste_types in waste_categories:
        return f"{waste_types.capitalize()} jāliek {waste_categories[waste_types]} konteinerā."
    else:
        return "Atkritumu veids nav sarakstā. Lūdzu mēģiniet vēlreiz!"

def main():
    print("Sveicināti atkritumu šķirošanas sistēmā!")
    while True:
        waste_input = input("Ievadiet atkritumu veidu (vai 'exit' lai beigtu darbu): ").strip()

        if waste_input.lower() == 'exit':
            print("Paldies, ka izmantojāt atkritumu šķirošanas sistēmu!")
            break

        result = waste(waste_input)
        print(result)

if __name__ == "__main__":
    main()
