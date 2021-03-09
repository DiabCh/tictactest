from player_profile import  login, register


choices = {
    1:login,
    2:register,
    3:"other function"
}


while True:
    print("1,2,3")
    choice = input("choice")
    if not choice.isdecimal():
        continue
    choice = int(choice)
    func = choices.get(choice)
    if not func: 
        print("Invalid option!")
        continue
    func()


    
# for acc in saved_data:
#     if acc["username"] == username:
#         account = acc
#         break
# else:#ONLY RUNS IF BREAK IS NOT HIT
#     account = None