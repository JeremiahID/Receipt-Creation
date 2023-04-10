company_name=("coding temple, inc.")
company_address =("283 Franklin st." + "\n" + "\t\t\t" + "boston, MA.")
P1_Price = 449.95
P2_Price = 579.99
P3_Price = 124.89
print("*" *75)
print("\t\t\t{}". format(company_name.title()))
print("\t\t\t{}". format(company_address))
print("=" *75)
print("\t\t" "Product Name" "\t\t" "Product Price")
P1_name,P1_Price = "book" , 449.95
print("\t\t {}\t\t\t${}". format (P1_name.title(),P1_Price))
P2_name,P2_Price = "computer" , 579.99
print("\t\t {}\t\t${}". format (P2_name.title(),P2_Price))
P3_name,P3_Price = "monitor" , 124.89
print("\t\t {}\t\t${}". format (P3_name.title(),P3_Price))
Total= P1_Price + P2_Price + P3_Price
print("=" *75)
print("\t"+"\t"+"\t" +"\t"+ "\t"+"Total")
print("\t\t\t\t\t$" + '{:.2f}'. format(Total))
print("=" *75 + "\n")

print("\t\t""Thanks for shopping with us today!" + "\n")

print("*" *75)
