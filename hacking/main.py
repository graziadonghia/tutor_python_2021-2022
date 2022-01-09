PRODUCTS_FILENAME = "prodotti.txt"
PURCHASES_FILENAME = "acquisti.txt"


def saveProducts(filename):
    products = {}
    f = open(filename, "r")

    for line in f:
        line_list = line.split(" ")
        prod_code = line_list[0]
        vendor_code = line_list[1].replace("\r\n", "")
        products[prod_code] = vendor_code

    f.close()
    return products


def checkPurchases(filename, products):
    purchase = {}
    suspects = []
    f = open(filename, "r")
    for line in f:
        line_list = line.split(" ")
        prod_code = line_list[0]
        vendor_code = line_list[1].replace("\r\n", "")
        if prod_code in purchase.keys():
            purchase[prod_code].append(vendor_code)
        else:
            purchase[prod_code] = vendor_code.split()
        if vendor_code != products[prod_code]:
            suspects.append(prod_code)
    f.close()

    return purchase, suspects

def main():

    products = saveProducts(PRODUCTS_FILENAME)
    print("Elenco transazioni sospette")

    purchase, suspects = checkPurchases(PURCHASES_FILENAME, products)
    for prod in purchase.keys():
        if prod in suspects:
            print("Codice prodotto: "+prod)
            print("Rivenditore ufficiale: "+products[prod])
            print("Lista rivenditori: "+str(purchase[prod]))
            print("\n")

main()