#menu asking player name and the mode they want to play
#player vs player
#player vs AI
#Logging game results csv file
import csv
store=[]
init=[1,2,3,4,5,6,7,8,9]
position=int()
player1=str()
player2=str()
squares=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

   
def win(playerturn:int)->True:
    global player1,player2,squares
    if playerturn%2!=0:
     eval=+1000
     print(f'{player1} wins {eval}')
     with open('Tictactoe.csv','a',newline='') as Game:
        feildnames=['Player1','Player2','Winner']
        csv_writer=csv.DictWriter(Game,fieldnames=feildnames)
        csv_writer.writerow({'Player1':f'{player1}','Player2':f'{player2}','Winner':f'{player1}'})
        squares=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
     main() 
    else:
     eval=-1000
     print(f'{player2} wins {eval}')
     with open('Tictactoe.csv','a',newline='') as Game:
        feildnames=['Player1','Player2','Winner']
        csv_writer=csv.DictWriter(Game,fieldnames=feildnames)
        csv_writer.writerow({'Player1':f'{player1}','Player2':f'{player2}','Winner':f'{player2}'})
        squares=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
     main()
    
def board():
    #making the board
    #based heavily on matrix
    squares=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    #what 2 players see
    print(f'{squares[0]}'.replace(',','|'))
    print(f'{squares[1]}'.replace(',','|'))
    print(f'{squares[2]}'.replace(',','|'))
    i=0
    run=True
    init=[1,2,3,4,5,6,7,8,9]
    while run:
        global store,position
        position=input('Where do you want to place it?')
        try:
            position=int(position)
            i+=1
            #you can use the linear search but with this loop it is O(N)^3
            if position>=1 and position<=3:
                init.remove(position)
                print(init)
                row=0
                col=position-1
                if i%2!=0:
                    squares[row][col]='X'
                    print(f'{squares[0]}'.replace(',','|'))
                    print(f'{squares[1]}'.replace(',','|'))
                    print(f'{squares[2]}'.replace(',','|'))
                    #checking for wins
                    if i>3:
                     for o in range(3):  
                      if squares[o]==['X','X','X']:
                          win(i)
                          break
                      if squares[0][o]== squares[1][o]==squares[2][o]:
                          win(i)
                          break
                      if squares[0][0]==squares[1][1]==squares[2][2]:
                          win(i)
                          break            
                else:
                    squares[row][col]='O'
                    print(f'{squares[0]}'.replace(',','|'))
                    print(f'{squares[1]}'.replace(',','|'))
                    print(f'{squares[2]}'.replace(',','|'))
                    if i > 3:
                     for o in range(3):  
                      if squares[o]==['O','O','O']:
                          win(i)
                          break
                      if squares[0][o]== squares[1][o]==squares[2][o]:
                          win(i)
                          break
                      if squares[0][0]==squares[1][1]==squares[2][2]:
                          win(i)
                          break    
                    #checking for wins   
            if position>=4 and position<=6:
                init.remove(position)
                print(init)
                row=1
                col=position-4
                if i%2!=0:
                    squares[row][col]='X'
                    print(f'{squares[0]}'.replace(',','|'))
                    print(f'{squares[1]}'.replace(',','|'))
                    print(f'{squares[2]}'.replace(',','|'))

                    #checking for wins
                    if i>3:
                      for o in range(3):  
                       if squares[o]==['X','X','X']:
                          win(i)
                          False
                          break
                       if squares[0][o]== squares[1][o]==squares[2][o]:
                          win(i)
                          False
                          break
                       if squares[0][0]==squares[1][1]==squares[2][2]:
                          win(i)
                          False
                          break    
                else:
                    squares[row][col]='O'
                    print(f'{squares[0]}'.replace(',','|'))
                    print(f'{squares[1]}'.replace(',','|'))
                    print(f'{squares[2]}'.replace(',','|'))
                    #checking for wins
                    if i>3:
                      for o in range(3):  
                       if squares[o]==['O','O','O']:
                          win(i)
                          break
                       if squares[0][o]== squares[1][o]==squares[2][o]:
                          win(i)
                          break
                       if squares[0][0]==squares[1][1]==squares[2][2]:
                          win(i)
                          break   
            if position>=7 and position<=9:
                init.remove(position)
                print(init)
                row=2
                col=position-7
                if i%2!=0:
                    squares[row][col]='X'
                    print(f'{squares[0]}'.replace(',','|'))
                    print(f'{squares[1]}'.replace(',','|'))
                    print(f'{squares[2]}'.replace(',','|'))
                    #checking for wins
                    if i>3:
                      for o in range(3):  
                       if squares[o]==['X','X','X']:
                          win(i)
                          break
                       if squares[0][o]== squares[1][o]==squares[2][o]:
                          win(i)
                          break
                       if squares[0][0]==squares[1][1]==squares[2][2]:
                          win(i)
                          break
                              
                else:
                    squares[row][col]='O'
                    print(f'{squares[0]}'.replace(',','|'))
                    print(f'{squares[1]}'.replace(',','|'))
                    print(f'{squares[2]}'.replace(',','|'))
                    #checking for wins
                    if i>3:
                      for o in range(3):  
                       if squares[o]==['O','O','O']:
                          win(i)
                          run=False
                          break
                       if squares[0][o]== squares[1][o]==squares[2][o]:
                          win(i)
                          run=False
                          break
                       if squares[0][0]==squares[1][1]==squares[2][2]:
                          win(i)
                          run=False
                          break   
            if i==9:
                print(f'{squares[0]}'.replace(',','|'))
                print(f'{squares[1]}'.replace(',','|'))
                print(f'{squares[2]}'.replace(',','|'))
                with open('Tictactoe.csv','a',newline='') as Game:
                    feildnames=['Player1','Player2','Winner']
                    csv_writer=csv.DictWriter(Game,fieldnames=feildnames)
                    csv_writer.writerow({'Player1':f'{player1}','Player2':f'{player2}','Winner':'Draw'})
                squares=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
                main() 
                break                     
        except:
            print('please enter a whole number 1 to 9')
            i-=1    

def option1():
    pass
def option2():
    #player vs player so we must take player names first
    global player1,player2
    player1=input('What is the name of player 1')
    player2=input('What is the name of player 2')
    
def option3():
    #player vs AI only one players name must be taken
    player=input('Name of player against AI?')
    print(player)
def main():
    print("-------Menu---------")
    print("\n")
    print("1.Game logs")
    print("2.Player vs Player")
    print("3.Player vs AI")
    while True:
        select=input()
        try:
            select=int(select)
            if select==1:
                option1()
            elif select==2:
                option2()
                board()
            elif select==3:
                option3()
                board()
                #we as a player have one turn while the AI gets one turn.
            else:
                print("Please enter the selection numbers 1,2 or 3")    
        except:
           print("Please enter the selection numbers 1,2 or 3")
main()


      

  