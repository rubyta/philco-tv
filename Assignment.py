#Name: Excelia Puspa Dewi
#Date: Nov. 17, 2011
#Purpose: will calculate the cost of purchasing a meal

#const real TAX_PERCENT = 0.13
#const real BURGER_COST = 0.99
#const real FRIES_COST = 0.79
#const real SODA_COST = 1.09
#const real MAX_BURGER = 20
#const real MIN_BURGER = 0
#const real MAX_FRIES = 20
#const real MIN_FRIES = 0
#const real MAX_SODA = 20
#const real MAX_SODA = 20
#String item_name_burger, item_name_fries, item_name_soda

BURGER_COST = 0.99
FRIES_COST = 0.79
SODA_COST = 1.09

MAX_BURGER = 20
MIN_BURGER = 0

MAX_FRIES = 20
MIN_FRIES = 0

MAX_SODA = 20
MIN_SODA = 0

item_name_burger="burger"
item_name_fries="fries"
item_name_soda="soda"

TAX_PERCENT = 0.13

def main():
    #int order_num, menu, leftover_burger, burger, total_burger, leftover_fries, fries, total_fries, leftover_soda, soda, total_soda
    #real burger_price, fries_price, soda_price, total_cost, total_tax, final_price

    print ("=========================================================================")

    order_num = 1
    while order_num > 0:
        order_num = get_order_number()
        if(order_num == 0):
           break

        print("START ORDER:%d" %order_num)

        #Initial variable must be set every time start new order 
        total_burger = 0
        total_fries = 0
        total_soda = 0
        leftover_burger = 0
        leftover_fries = 0
        leftover_soda = 0

        menu = 0
        while(menu !=4 ):
            menu = show_menu(item_name_burger,item_name_fries,item_name_soda )
            if(menu == 1):
                leftover_burger = MAX_BURGER - total_burger
                print("you can order %d - %d %s" %(MIN_BURGER,leftover_burger,item_name_burger))
                burger = get_item(item_name_burger,MIN_BURGER,leftover_burger)
                total_burger = total_burger + burger
                                    
            elif(menu == 2):
                leftover_fries = MAX_FRIES - total_fries
                print("you can order %d - %d %s" %(MIN_FRIES, leftover_fries, item_name_fries))
                fries = get_item(item_name_fries,MIN_FRIES,leftover_fries)
                total_fries = total_fries + fries
                
            elif(menu == 3):
                leftover_soda = MAX_SODA - total_soda
                print("you can order %d - %d %s" %(MIN_SODA, leftover_soda, item_name_soda))
                soda = get_item(item_name_soda,MIN_SODA,leftover_soda)
                total_soda = total_soda + soda
                
            else:
                break
            
        burger_price = calculate_cost(total_burger, BURGER_COST)
        fries_price = calculate_cost(total_fries, FRIES_COST)
        soda_price = calculate_cost(total_soda, SODA_COST)
                
        total_cost = calculate_total(burger_price, fries_price, soda_price)
        total_tax = calculate_tax(total_cost,TAX_PERCENT)
        final_price = calculate_final(total_cost, total_tax) 
        
        print_result(item_name_burger, item_name_fries, item_name_soda, total_burger, total_fries, total_soda, burger_price, fries_price, soda_price, total_cost, total_tax, final_price)

        return
#################################################################################################
def show_menu(burger_item, fries_item, soda_item ):
    #int get_menu
    #const real MIN = 1
    #const real MAX = 4
    MIN_MENU = 1
    MAX_MENU = 4

    
    print("------------------------------- M E N U --------------------------------")    
    print("Enter 1 for Yum Yum %s" %burger_item)
    print("Enter 2 for Grease Yum %s" %fries_item)
    print("Enter 3 for %s Yum" %soda_item)
    print("Enter 4 to end order")

    print(" ")
    get_menu = int(input("Enter now:"))
    while(get_menu < MIN_MENU or get_menu > MAX_MENU):
        print("please enter number between %d and %d"%(MIN_MENU, MAX_MENU))
        get_menu = int(input("Enter now:"))
    print(" ")
     
    return get_menu
#################################################################################################
def get_order_number():
    #int order_number

    print ("============================= NEW ORDER =================================")
   
    order_number = int(input("Please enter order number (>=0). Enter 0 to stop the program:"))
    while(order_number < 0):
        print("Input Error!")
        order_number = int(input("Please enter order number (>0). Enter 0 to stop the program:"))
    return order_number

##################################################################################################
def get_item(item_name, item_min, item_max):
#String item_name
#int item_min, item_max, number_item
                 
    number_item = int(input("Enter the number of %s you want:" %item_name))
    while (number_item < item_min or number_item > item_max):
        print("input error!")
        print("you can order the %d - %d %s." %(item_min, item_max, item_name))
        number_item = int(input("Enter the number %s you want:" %item_name ))              
    
    return number_item
##################################################################################################
def calculate_cost(total_item, cost_item):
    #real cost, total_item, cost_item

    cost = total_item*cost_item
            
    return cost
###################################################################################################
def calculate_tax(item_cost, taxes):
    #real tax_cost, item_cost, taxes

    tax_cost = item_cost*taxes
                          
    return tax_cost
###################################################################################################
def calculate_total(burger_cost, fries_cost, soda_cost):
    #real total, burger_cost, fries_cost, soda_cost

    total = burger_cost + fries_cost + soda_cost

    return total
###################################################################################################
def calculate_final(tax,cost):
    #real final_cost, tax, cost

    final_cost = tax + cost

    return final_cost
###################################################################################################
def print_result(item_name_burger, item_name_fries, item_name_soda, total_burger, total_fries, total_soda, burger_price, fries_price, soda_price, total_cost, total_tax, final_price):
    
    print("--------------------Thanks for your order-----------------------")
    print(" ")

    print("======================= R E C E I P T =========================")
    print("Number of %s ordered  : %d" %(item_name_burger,total_burger) )
    print("Sub-total ($%.2f each)    : $%.2f" %(BURGER_COST, burger_price) )
    print("Number of %s ordered   : %d" %(item_name_fries,total_fries) )
    print("Sub-total ($%.2f each)    : $%.2f" %(FRIES_COST, fries_price) )
    print("Number of %s ordered    : %d" %(item_name_soda,total_soda) )
    print("Sub-total ($%.2f each)    : $%.2f" %(SODA_COST, soda_price) )
    print("Total                     : $%.2f" %total_cost)
    print("Tax at %.d%%                : $%.2f" %(TAX_PERCENT*100, total_tax) )  					
    print("-----------------------------------------------------------------")
    print("Final Purchase Price      : $%.2f" %final_price)
    return
######################################################################################################
main()
print("Finish...Thank you for using this program.")





