import random
end = False
while(not end):
    ui=input("Scissors(0), Rock (1), Paper (2), Lizard (3), Spock (4) ")
    while((ui!="0")and(ui!="1")and(ui!="2")and(ui!="3")and(ui!="4")):
        ui=input("Scissors(0), Rock (1), Paper (2), Lizard (3), Spock (4) ")
    ci=random.randint(0,4)
    ui = int(ui)
    if ui == ci:
        results="It's a draw"
    elif (ui==1 and ci==2) or (ui==0 and ci==1) or (ui==2 and ci==0)or(ui==3 and ci==1)or(ui==4 and ci==2)or(ui==3 and ci==0)or(ui==1 and ci==4)or(ui==2 and ci==3)or(ui==4 and ci==3)or(ui==0 and ci==4):
        results = "You lose"
    else:
        results = "You win"
    #assigning the names to the numbers
    if ui == 0:
        ui = "Scissors"
    elif ui==1:
        ui="Rock"
    elif ui ==2:
        ui="Paper"
    elif ui == 3:
        ui="Lizard"
    elif ui == 4:
        ui="Spock"
    if ci == 0:
        ci = "Scissors"
    elif ci==1:
        ci="Rock"
    elif ci ==2:
        ci="Paper"
    elif ci == 3:
        ci="Lizard"
    elif ci == 4:
        ci="Spock"
    print(f"{results}. You threw {ui} and the computer threw {ci}.")
    end = input("Would you like to play again? (y/n) ")
    while((end != "y") and (end!="n")):
        end = input("Would you like to play again? (y/n) ")
    if end == "y":
        end = False
    else:
        end = True
