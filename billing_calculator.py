import math


while True:
    ask = input("do you wanna sum the amount or add discount(sum or disc or q to quit) : ")
    comment = "thanks for using our calculator"

    if ask == "sum":
        sum=0
        
        while True:
            price = input('enter your price OR "sum" to add total - ')

            if price == "q":
                print(f"""
            {comment.title()}
            the total sum is {sum}
            
            """)
                break
            
            elif price == "sum" :
                print(f"""
            {comment.title()}
            the total sum is {sum}
            
            """)
                sum = 0

            elif price != "sum":
                sum = sum + int(price)
                print(f"""sum till now is {sum}
""")


    elif ask =="q":
        print(f'''
            {comment.title()}
        ''')
        break


    elif ask =="disc":
        while True:
            amount = input("enter the amount : ")

            if amount == "q" :
                print(f"""
                {comment.title()}
                """)
                break
            
            else:
                amt = int(amount)

                discount = input("Enter discount percent : ")

                if discount =="q":
                    print(f"""
                    {comment.title()}
                    """)
                    break

                else:
                    dsc = int(discount)

                    disc_price = amt * (100-dsc)/100
                    print(f"""
                    {comment.title()}
                    Your Total Amount is {math.floor(disc_price)}
                    """)