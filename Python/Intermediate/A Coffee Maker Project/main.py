import menu
import coffee_maker
import money_machine

cm=coffee_maker.CoffeeMaker()
m=menu.Menu()
mm=money_machine.MoneyMachine()


machine='on'
while machine!='off':
    orderName=input(f"""What would you like to have?
    {m.get_items()}
  """)
    order=''

    if orderName=="REPORT":
        cm.report()
        mm.report()
    elif orderName=="off":
        print("\nTurning off")
        machine=orderName
        print("\nThank you")
    else:
        order=m.find_drink(orderName)

    if order!='':
        permission=cm.is_resource_sufficient(order)
        if permission:
            permission=mm.make_payment(order.cost)
            if permission:
                cm.make_coffee(order)
                print("\n"*2)
