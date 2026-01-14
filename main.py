import  pandas  as pd 

def welcome_message():
    print("welcome to our cafe !")
    menu_type=input("\n what do you like to have drinks or snacks ?? : ").lower()
    if menu_type == "drinks" :
        menu = pd.read_csv("drinks.csv")
    elif menu_type == "snacks" :
        menu = pd.read_csv("snacks.csv")
      
    else :
        print("\n sorry we have just drinks and snacks") 
        return None
    
    print("\n______________menu________________\n")
    menu.columns = menu.columns.str.strip().str.lower()          

    for index,row in menu.iterrows():
        print(f"{index+1} . {row['item']:<30} -  rs {row['price']}")
    
    return menu
        

def order(menu):
    total_price = 0

    while True :
        for index,row in menu.iterrows():
            print(f"{index+1}.{row['item']:<30}.{row['price']}")
        item_number = int(input("\n enter the item number you want to order : "))
        quantity = int(input("\n enter the quantity you want :"))

        item_name = menu.loc[item_number -1,"item"]
        order_price = menu.loc[item_number -1,"price"]*quantity

        total_price += order_price
 
        print(f"\n your ordered {quantity},{item_name} :")
        print(f"\n current total: rs {total_price}")
 
        more = input("\n do you want to order anything else  ?  (y/n) : ").lower ()
        if more != "y":
          break
    
    print('\n thank you for ordering, your order will be delivered soon !')
    print(f"\n your final total i: Rs {total_price}")    

    
if __name__ == "__main__":
    menu = welcome_message()  
    if menu is not None:
       order(menu)      
