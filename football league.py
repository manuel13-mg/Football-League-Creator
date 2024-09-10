def CreateDatabase():  ## Default
    import mysql.connector as m
    con=m.connect(host='localhost',user='root',passwd='student')
    cur=con.cursor()
    qry= "Create Database Tournament;"
    cur.execute(qry)
    con.close()
#CreateDatabase()

def create_tournament_table():   ## Default
    import mysql.connector as m
    con=m.connect(host='localhost',user='root',passwd='student',database='Tournament')
    cur=con.cursor()
    qry= 'CREATE TABLE TOURNAMENT \
          (T_no INT(3) PRIMARY KEY\
          ,T_name varchar(100))'
    cur.execute(qry)
    con.close()
create_tournament_table()
  
def League():
    import mysql.connector as m
    con=m.connect(host='localhost',user='root',passwd='student',database='Tournament')
    cur=con.cursor()
    global T_no
    T_no=int(input('Enter the league no: '))
    global T_name
    T_name= input('Enter the league name: ')
    qry= "CREATE TABLE {}(\
         TEAMCODE VARCHAR(20) PRIMARY KEY,\
         TEAMNAME VARCHAR(20) NOT NULL,\
         MATCHESPLAYED INT,\
         WIN INT,\
         LOSE INT,\
         DRAW INT,\
         POINTS INT,\
         GOALSFOUND INT,\
         GOALSALLOWED  INT,\
         GOALDIFFERENCE INT\
         );"
    cur.execute(qry.format(T_name))
    print("LEAGUE CREATED SUCCESFULLY")
    con.close()
#League()

def insert_tournament():  ##  Default
    import mysql.connector as m
    con=m.connect(host='localhost',user='root',passwd='student',database='Tournament')
    cur=con.cursor()
    qry="INSERT INTO TOURNAMENT\
         VALUES({},'{}')"
    cur.execute(qry.format(T_no,T_name))
    con.commit()
    con.close()
#insert_tournament()
    
def TeamDetails():
    import mysql.connector as m
    con=m.connect(host='localhost',user='root',passwd='student',database='Tournament')
    cur=con.cursor()
    T_no=int(input('Enter the League no: '))
    qry="select T_name from tournament where t_no={}"
    cur.execute(qry.format(T_no))
    rs=cur.fetchone()
    T_name= str(rs[0])
    while True:
        TeamCode=input("enter Team Code: ")
        TeamName=input("enter Team name: ")
        MatchesPlayed=int(input("enter the no of matches played: "))
        Win=int(input("enter the no of wins: "))
        Lose=int(input("enter the number of losses: "))
        Draw=int(input("enter the number of draws: "))
        Points= Win*3+Draw*1+Lose*0
        GoalsFound=int(input("enter the no of goals scored: "))
        GoalsAllowed=int(input("enter the no of goals conceded: "))
        GoalDifference= GoalsFound-GoalsAllowed
        qry1="INSERT INTO "+ T_name +" Values('{}','{}',{},{},{},{},{},{},{},{})"
        cur.execute(qry1.format(TeamCode,TeamName,MatchesPlayed,Win,Lose,Draw,Points,GoalsFound,GoalsAllowed,GoalDifference))
        con.commit()
        x=input("do you want to continue y/n: ")
        if x.lower()=='n':
            break
    con.close()
#TeamDetails()


def TeamRecord():
    import mysql.connector as m
    con=m.connect(host='localhost',user='root',passwd='student',database='Tournament')
    cur=con.cursor()
    T_no=int(input('Enter the League no: '))
    qry="select T_name from tournament where t_no={}"
    cur.execute(qry.format(T_no))
    rs=cur.fetchone()
    T_name= str(rs[0])
    qry= "SELECT * FROM "+T_name+" ORDER BY POINTS DESC, GOALDIFFERENCE  DESC;"
    cur.execute(qry)
    rs=cur.fetchall()
    print('-'*63)
    print('|TEAM_CODE|','|TEAM_NAME|','|MP|','|W |','|L |','|D |','|P |','|GF|','|GA|','|GD|')
    print('-'*63)
    for i in rs:
        print('|'+'   '+str(i[0])+' '*len(str(i[0]))+'|',\
              '|'+'   '+ str(i[1])+' '*(6-len(str(i[1])))+'|'+' '+\
              '|'+''+str(i[2])+''+'|'+' '+\
              '|'+''+str(i[3])+''+'|'+' '+\
              '|'+''+str(i[4])+' '+'|'+' '+\
              '|'+''+str(i[5])+' '+'|'+' '+\
              '|'+''+str(i[6])+''+'|'+' '+\
              '|'+''+str(i[7])+''+'|'+' '+\
              '|'+''+str(i[8])+''+'|'+' '+\
              '|'+''+str(i[9])+''+'|')
        print('-'*63)
# TeamRecord()

def TeamStats():
    import mysql.connector as m
    con=m.connect(host='localhost',user='root',passwd='student',database='tournament')
    cur=con.cursor()
    T_no=int(input('Enter the League no: '))
    qry="select T_name from tournament where t_no={}"
    cur.execute(qry.format(T_no))
    rs=cur.fetchone()
    T_name= str(rs[0])
    teamcode=input('Enter Team Code you want:')
    qry='select * from '+T_name+' where teamcode="{}"'
    cur.execute(qry.format(teamcode))
    rs=cur.fetchone()
    print('-'*63)
    print('|TEAM_CODE|','|TEAM_NAME|','|MP|','|W |','|L |','|D |','|P |','|GF|','|GA|','|GD|')
    print('-'*63)
    print('|'+'   '+str(rs[0])+' '*len(str(rs[0]))+'|',\
          '|'+'   '+ str(rs[1])+' '*(6-len(str(rs[1])))+'|'+' '+\
          '|'+''+str(rs[2])+''+'|'+' '+\
          '|'+''+str(rs[3])+''+'|'+' '+\
          '|'+''+str(rs[4])+' '+'|'+' '+\
          '|'+''+str(rs[5])+' '+'|'+' '+\
          '|'+''+str(rs[6])+''+'|'+' '+\
          '|'+''+str(rs[7])+''+'|'+' '+\
          '|'+''+str(rs[8])+''+'|'+' '+\
          '|'+''+str(rs[9])+''+'|')
    print('-'*63)  
    con.close()
# TeamStats()


def Update():
    import mysql.connector as m
    con=m.connect(host='localhost',user='root',passwd='student',database='Tournament')
    cur=con.cursor()
    T_no=int(input('Enter the League no: '))
    qry="select T_name from tournament where t_no={}"
    cur.execute(qry.format(T_no))
    rs=cur.fetchone()
    T_name= str(rs[0])
    while True:
        TeamCode= input('Enter the team code: ')
        choose= int(input('''CHOOSE 1 for updating the Team Name\
                         CHOOSE 2 for updating the Team code\
                         Enter your choice:'''))
        if choose == 1:
            new= input('Enter the new team name: ')
            qry="UPDATE "+T_name+" SET TEAMNAME='{}' WHERE TEAMCODE='{}' ;"
            cur.execute(qry.format(new,TeamCode))
            con.commit()
            print('UPDATED SUCCESFULLY!!!')
        elif choose == 2:
            new= input('Enter the new Team code: ')
            qry="UPDATE "+T_name+" SET TEAMCODE='{}'WHERE TEAMCODE='{}' ;"
            cur.execute(qry.format(new,TeamCode))
            con.commit()
            print('UPDATED SUCCESFULLY!!!')
        else:
            print('INVALID CHOICE!!!')
        x= input('Do you want to continue(y/n): ')
        if x.lower()=='n':
            break
#Update()




def Delete():
    import mysql.connector as m
    con=m.connect(host='localhost',user='root',passwd='student',database='Tournament')
    cur=con.cursor()
    T_no=int(input('Enter the League no: '))
    qry="select T_name from tournament where t_no={}"
    cur.execute(qry.format(T_no))
    rs=cur.fetchone()
    T_name= str(rs[0])
    qry= 'Drop table '+ T_name
    cur.execute(qry)
    print("Table deleted succesfully")
    qry='Delete From Tournament where T_no={}'
    cur.execute(qry.format(T_no))
    con.commit()
    con.close()
#Delete()

def Disp_tournament():
    import mysql.connector as m
    con=m.connect(host='localhost',user='root',passwd='student',database='Tournament')
    cur=con.cursor()
    qry= "SELECT * FROM Tournament;"
    cur.execute(qry)
    rs=cur.fetchall()
    
def Disp_tournament():
    import mysql.connector as m
    con=m.connect(host='localhost',user='root',passwd='student',database='Tournament')
    cur=con.cursor()
    qry= "SELECT * FROM Tournament;"
    cur.execute(qry)
    rs=cur.fetchall()
    print('-'*16)
    print('|'+'T_no'+'|','|'+'T_name'+' '+'|')
    print('-'*16)
    for i in rs:
        print('|'+str(i[0])+'   '+'|','|'+str(i[1])+' '*(7-len(str(i[1])))+'|')
    print('-'*16)
# Disp_tournament()

def Main_Menu():
    while True:
        print('-'*50)
        print("Football Tournament")
        print("-"*50)
        print("Enter")
        print("1:For Creating New League")
        print("2:For Displaying Leagues")
        print("3:For Inserting Team Details")
        print("4:For League Record")
        print("5:For Team Stats")
        print("6:For Updating")
        print("7:To Delete")
        print("-"*50)
        print()
        print('*'*50)
        x=int(input("Enter your choice: "))
        if x==1:
            League()
            insert_tournament()
        elif x==2:
            Disp_tournament()
        elif x==3:
            TeamDetails()
        elif x==4:
            TeamRecord()
        elif x==5:
            TeamStats()
        elif x==6:
            Update()
        elif x==7:
            Delete()
        else:
            print("Your choice is invalid")
        a=input("Do you want to continue? y/n: ")
        if a.lower()=='n':
            break
        else:
            print("Thank you!")
Main_Menu()    
