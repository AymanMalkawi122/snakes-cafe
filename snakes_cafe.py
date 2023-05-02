quit_flag=False
menu={
"Wings":0,
"Cookies":0,
"Spring Rolls":0,
"Salmon":0,
"Steak":0,
"Meat Tornado":0,
"A Literal Garden":0,
"Ice Cream":0,
"Cake":0,
"Pie":0,
"Coffee":0,
"Tea":0,
"Unicorn Tears":0
}

print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
''')
while not quit_flag:
    choice=input("> ")

    if choice=="quit":
        
        for item in menu:
            if menu[item]>0:
                print(f"** {menu[item]} order{'s' if menu[item]>1 else ''} of "
                +f"{item}**")
        quit_flag=True

    else:
        if choice in menu.keys():
            menu[choice] += 1
            print(f"** {menu[choice]} order{'s' if menu[choice]>1 else ''} of {choice}" 
            +" have been added to your meal **")
        