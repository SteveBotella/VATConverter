# VAT Converter software

import math


def vat_converter(duty_free, tax_value):
    """Convert the duty free price to all tax included price
    """
    vat_price = (duty_free * math.ceil(tax_value) / 100) + duty_free
    return vat_price


def main():
    """Main software."""
    # Ask to user a product name / demander un nom de produit à l'utilisateur
    product_name = input("Nom du produit : ")  # une chaîne de caractères

    # Ask to user a quantity / demander une quantité à l'utilisateur
    saisie = input("Quantité : ")  # une chaîne de caractères
    product_qty = float(saisie)  # convertie en un nombre réel

    # Ask to user a price without fee / demander un prix à l'utilisateur
    saisie = input("Prix HT : ")  # une chaîne de caractères
    duty_free = float(saisie)  # convertie en un nombre réel

    # Ask to user a fee / demander une tax à l'utilisateur
    saisie = input("Montant de la taxe : ")  # une chaîne de caractères
    tax_value = float(saisie)  # convertie en un nombre réel

    # Calculate the price / calculer le prix
    vat_price = vat_converter(duty_free, tax_value)

    # Display the price with taxes / afficher le prix TTC d'un produit à l'utilisateur
    print("Le prix TTC de", product_name, "est de", vat_price, "€")

    # Calculate stock price / calculer le prix du stock
    total_price = vat_price * product_qty

    # Calculate stock fee / calculer le montant de la tax du stock
    total_fee = total_price - (duty_free * product_qty)

    # Calculate the discount / calculer le montant de la remise
    discount = 0
    if total_price > 1000:
        discount = total_price * 12 / 100
        total_price = total_price - discount

    # Display stock price (all taxes included)/ afficher le prix TTC du stock à l'utilisateur
    print("Le total TTC du stock de", product_name, "est de", total_price, "€ (dont taxes de", total_fee, "- remise de",
          discount, ")")


if __name__ == "__main__":
    main()
