PRODUCTS_FILENAME = "prodotti.txt"
SALES_FILENAME = "acquisti.txt"


def saveProducts(filename):
    products = {}
    f = open(filename, "r")
    for line in f:
        lineList = line.split(" ")
        prodCode = lineList[0]
        vendorCode = lineList[1].replace("\r\n", "")
        products[prodCode] = vendorCode
    f.close()

    return products


def checkSales(filename, products):
    sales = {}
    suspects = []
    f = open(filename, "r")
    for line in f:
        lineList = line.split(" ")
        prodCode = lineList[0]
        vendorCode = lineList[1].replace("\r\n", "")

        if prodCode in sales.keys():
            sales[prodCode].append(vendorCode)
        else:
            sales[prodCode] = vendorCode.split()
        if vendorCode != products[prodCode]:
            #suspect
            suspects.append(prodCode)
    f.close()

    return sales, suspects

def main():
    products = saveProducts(PRODUCTS_FILENAME)
    sales, suspects = checkSales(SALES_FILENAME, products)
    print("Elenco transazioni sospette")
    for prod in suspects:
        print("Codice prodotto: " + prod)
        print("Rivenditore ufficiale: " + products[prod])
        print("Lista rivenditori: " + str(sales[prod]))
        print("\n")

main()
