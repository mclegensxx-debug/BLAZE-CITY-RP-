import os
import random
import time
import json

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

has_job = "no"
money = 300
org = None
inv = []
name = None
wanted = 0
work_day = 0
hp = 100
luck = 3
bonus = "no"
fight = "yes"
intro = False
loop = False
energy = 100
cheat = 0
job_type = "none"
hacks_done = 0
escapes_done = 0
status = "citizen"
location = "downtown"
areas = ["downtown","market","mall","park"]
esc = None
cmd = None
esc_c = 0

ver = "v2.1"
web = "local"
ban_file = "banned.json"

def show_title():
    clear()
    print("========================>\n")
    print(f" BLAZE CITY {ver} ")
    print(" THE SYSTEM UPDATE")
    print(" Made by:MC LEGEND\n")
    print("========================>")

def is_banned(player_name):
    if os.path.exists(ban_file):
        with open(ban_file, "r") as f:
            banned_list = json.load(f)
            if player_name.lower() in banned_list:
                return True
    return False

def ban_player(player_name):
    banned_list = []
    if os.path.exists(ban_file):
        with open(ban_file, "r") as f:
            banned_list = json.load(f)
    if player_name.lower() not in banned_list:
        banned_list.append(player_name.lower())
    with open(ban_file, "w") as f:
        json.dump(banned_list, f)
        
def save():
    with open("save.json", "w") as f:
        json.dump({
            "money": money,
            "hp": hp,
            "name": name,
            "inv": inv,
            "wanted": wanted,
            "org": org,
            "has_job": has_job,
            "work_day": work_day,
            "luck": luck,
            "bonus": bonus,
            "fight": fight,
            "energy": energy,
            "cheat": cheat,
            "job_type": job_type,
            "hacks_done": hacks_done,
            "escapes_done": escapes_done,
            "status": status
        }, f)
        
def load():
    global money, hp, name, inv, wanted, org, has_job, work_day, luck, bonus, fight, energy, cheat, job_type, hacks_done, escapes_done, status
    try:
        with open("save.json", "r") as f:
            data = json.load(f)
            money = data["money"]
            hp = data["hp"]
            name = data["name"]
            inv = data["inv"]
            wanted = data["wanted"]
            org = data["org"]
            has_job = data["has_job"]
            work_day = data["work_day"]
            luck = data["luck"]
            bonus = data["bonus"]
            fight = data["fight"]
            energy = data["energy"]
            cheat = data["cheat"]
            job_type = data.get("job_type", "none")
            hacks_done = data.get("hacks_done", 0)
            escapes_done = data.get("escapes_done", 0)
            status = data["status"]
        return True
    except:
        return False

def show_inv():
    if not inv:
        print("Inventory: Empty")
    else:
        print("Inventory:")
        print('\n'.join(inv))

def del_save():
    if os.path.exists("save.json"):
        os.remove("save.json")

def game_info():
    clear()
    print("GAME INFO")
    print("\nMade by MC LEGEND")
    print(f"\nVersion: {ver}")
    print("\nSECRET JOBS:")
    print("- HACKER: Laptop > Web > System.exe")
    print("- FBI: Laptop > Web > FBI.work")
    print("- DRIVER: Escape 3 times")
    input("press enter to exit...")

# GAME(INTRO)
if os.path.exists("save.json"):
    load()
    loop = True
else:
    clear()
    if name == None:
        intro = True
        show_title()
        while intro:
            print("Enter your name\n")
            name = input("name:").strip()
            if name == "":
                print("A REAL NAME!")
                time.sleep(1)
                clear()
    
            else:
                if is_banned(name):
                	clear()
                	print("NOTICE")
                	print(f"\nThe player with the name '{name}' is currently\n PERMANENTLY BANNED")
                	break
                clear()
                loop = True
                intro = False
                break

peoples = ["john", "jake", "tom", "frank", "sam", "blaze", "henry", "jorald", "Mike"]

commands = ["1","2","3","4","5","6","7","8","9","10"]

# GAME(Main)
while loop:
    clear()
    if wanted >= 3 and status!= "police trace":
        clear()
        print("YOUR ON FBI/POLICE TRACE!")
        status = "police trace"
        time.sleep(1)
        os.system('clear')

    print(f"Name:{name} \nmoney:{money} || wanted:{wanted} || hp:{hp} || job:{job_type}")
    print(f"has a job: {has_job} || energy: {energy}")

    if status == "citizen":
        print("\nActions:")
        print("[1] open inventory")
        print("[2] find a job")
        print("[3] fight someone")
        print("[4] work(needs a job)")
        print("[5] Shop")
        print("[6] quit")
        print("[7] organization(join)")
        print("[8] sleep(Gain energy)")
        print("[9] Game info")
        print("[10] Open Laptop")
        save()
        cmd = input("> ")
        
        if cmd in commands:
        	if cheat >= 7:
        		clear()
        		print("BANNED")
        		print("the system detects that you\nUSE CHEATS or ABUSE CHEATS")
        		del_save()
        		ban_player(name)
        		break
        	else:
        		clear()
        		

        if cmd == "1029":
            clear()
            if cheat >= 5:
                print("confirming identity...")
                time.sleep(1)
                if name.lower() == "mc legend":
                    clear()
                    print("System:\n'DEV! HELLO THERE stop using the cheat code :)' ")
                    cheat += 1
                    time.sleep(1)
                    clear()
                    continue
                else:
                    clear()
                    print("BANNED:")
                    print("\nThis python Text-based RP ")
                    print("Has banned you for using Dev cheat codes")
                    del_save()
                    break
            else:
                money += 300
                print("DEV CHEAT CODE USED")
                print("\nare you MC LEGEND?")
                cheat += 1
                time.sleep(2)
                continue

        if money >= 3000:
            clear()
            print("= = = VICTORY= = =")
            print(f"\n you have earned {money} which %2 \nof people only can do!")
            print("\nRESPECT!")
            del_save()
            break

        if work_day == 10 and bonus!= "yes":
            clear()
            print("your boss thanks you by giving you bonus everytime you work")
            bonus = "yes"
            time.sleep(1)

        if hp <= 0:
            clear()
            print("You died....GAME OVER")
            del_save()
            break

        if cmd == "1":
            clear()
            show_inv()
            time.sleep(2)

        elif cmd == "2" and has_job!= "never":
            clear()
            faith = random.randint(1, 2)
            if wanted >= 2:
                print("THE BOSS KNEW YOUR WANTED!")
                print("AND CALLED THE POLICE!")
                del_save()
                break
            if faith == 1 and wanted <= 1 and has_job!= "yes":
                print("You got a job!")
                has_job = "yes"
                job_type = "local"
                time.sleep(1)
            else:
                if has_job == "yes":
                    print("you already have a job")
                else:
                    print("didn't find one")
                time.sleep(2)

        elif cmd == "3" and fight == "yes":
            clear()
            enemy = random.choice(peoples)
            print(f"enemy found {enemy}")
            enemy_hp = 100
            time.sleep(1)
            street_fight = True
            while street_fight:
                clear()
                print(f"your hp:{hp} || {enemy} hp:{enemy_hp}")
                print("\nActions")
                print("[1] punch || [2] run")
                if enemy_hp <= 0:
                    clear()
                    stoled = random.randint(1, 100)
                    print(f"YOU BEAT {enemy}!")
                    print(f"you earned {stoled}!")
                    energy -= 20
                    money += stoled
                    wanted += 1
                    time.sleep(2)
                    street_fight = False
                    break
                elif hp <= 0:
                    clear()
                    print(f"You have lost against {enemy}")
                    del_save()
                    break
                f = input("> ")
                if f == "1":
                    clear()
                    if "knife" in str(inv).lower():
                        dmg = random.randint(1, 30)
                        print(f"Knife Used! {dmg} damage!")
                        enemy_hp -= dmg
                        dmg2 = random.randint(1, 10)
                        print(f"\nenemy punch! \n you lost {dmg2} hp!")
                        hp -= dmg2
                        time.sleep(2)
                    else:
                        dmg = random.randint(1, 10)
                        print(f"You punch! {dmg} Damage!")
                        enemy_hp -= dmg
                        dmg2 = random.randint(1, 10)
                        print(f"\nEnemy punch! {dmg2} hp lost!")
                        hp -= dmg2
                        time.sleep(2)
                elif f == "2":
                    clear()
                    luck_roll = random.randint(1, 2)
                    if job_type == "driver":
                        luck_roll = 1
                    if luck_roll == 1:
                        print("You successfully Escaped!")
                        escapes_done += 1
                        if escapes_done >= 3 and job_type!= "driver":
                            print("\nSECRET UNLOCKED: GETAWAY DRIVER JOB!")
                            job_type = "driver"
                            has_job = "yes"
                        wanted += 1
                        time.sleep(1)
                        street_fight = False
                        break
                    else:
                        print("You failed to escape!")
                        dmg2 = random.randint(1, 10)
                        print(f"{enemy} punch you! {dmg2} hp lost!")
                        hp -= dmg2
                        time.sleep(1)

        elif cmd == "4" and has_job!= "never":
            clear()
            if has_job == "yes":
                if job_type == "fbi":
                    print("you work for FBI")
                    stoled = random.randint(100, 200)
                    print(f"FBI paycheck: ${stoled}")
                    money += stoled
                    wanted = max(0, wanted - 1)
                    time.sleep(1)
                elif job_type == "hacker":
                    if energy <= 19:
                        print("Too tired sleep first")
                        time.sleep(1)
                    else:
                        stoled = random.randint(50, 150)
                        print(f"hacked a bank! earned {stoled}!")
                        money += stoled
                        energy -= 20
                        time.sleep(1)
                else:
                    if energy <= 19:
                        print("Too tired sleep first")
                        time.sleep(1)
                    else:
                        stoled = random.randint(1, 100)
                        work_day += 1
                        print(f"day {work_day},done! earned {stoled}!")
                        money += stoled
                        energy -= 20
                        if bonus == "yes":
                            stoled = random.randint(1, 50)
                            print(f"\nbonus: {stoled}+")
                            money += stoled
                        time.sleep(1)
            else:
                print("find a job first")
                time.sleep(1)

        elif cmd == "5":
            clear()
            print("= =SHOP= =")
            print(f"Your money: ${money}")
            print("$20 [1] healing potion (hp 15+)")
            print("$30 [2] knife (+10% win chance)")
            print("$100 [3] bribe police (wanted level -1)")
            print("$50 [4] Monster drink (+50 energy)")
            print("$100 [5] real web(web money unlock)")
            buyed = input("> ").strip()
            if buyed == "1" and money >= 20:
                if hp <= 99:
                    money -= 20
                    inv.append("healing potion")
                    hp = min(100, hp + 15)
                    print("Healed +15 hp!")
                    time.sleep(1)
                else:
                    print("full hp no need")
                    time.sleep(1)
            elif buyed == "4" and money >= 50:
                money -= 50
                energy = min(100, energy + 50)
                print("\nENERGY DRINK! +50 energy")
                time.sleep(1)
            elif buyed == "5" and money >= 100:
            	web = "real"
            	money -= 100
            elif buyed == "2" and money >= 30:
                if "knife" in inv:
                    print("already have Knife!")
                    time.sleep(1)
                else:
                    money -= 30
                    inv.append("knife")
                    print("Bought knife! Better odds!")
                    time.sleep(1)
            elif buyed == "3" and money >= 100:
                if wanted >= 1:
                    money -= 100
                    wanted = max(0, wanted - 1)
                    print("BRIBED!")
                    time.sleep(1)
                else:
                    print("no need")
                    time.sleep(1)
            else:
                print("we don't have that or your broke")
                time.sleep(1)

        elif cmd == "6":
            clear()
            print("closing program...")
            time.sleep(2)
            clear()
            print("you wanna delete save?\ny/n")
            asking = input("> ")
            if asking.lower() == "y":
                del_save()
            else:
                print("closed")
            break

        elif cmd == "8":
            clear()
            if energy >= 80:
                print("still not tired")
                time.sleep(1)
            else:
                print("sleeping...\nplease wait")
                time.sleep(3)
                energy = 100

        elif cmd == "7":
            clear()
            if org == "gang" or org == "anti-gov" or org == "peace" or org == "fbi":
                print("you already joined a organization")
                time.sleep(1)
            else:
                print("\n[1] Gang orga(+$100,-1 wanted level")
                print("\n[2] Anti-Gov orga(can't work/fired from job, can't fight people)")
                print("\n[3] Peace orga(can't fight, +$200)")
                ask = input("> ")
                if ask == "1":
                    clear()
                    print("orga Joined!")
                    org = "gang"
                    money += 100
                    wanted = max(0, wanted - 1)
                    time.sleep(1)
                elif ask == "2":
                    clear()
                    print("orga joined!")
                    has_job = "never"
                    org = "anti-gov"
                    fight = "no"
                    time.sleep(1)
                elif ask == "3":
                    clear()
                    org = "peace"
                    print("orga joined!")
                    fight = "no"
                    money += 200
                    time.sleep(1)
                else:
                    clear()
                    print("unknown orga")
                    time.sleep(1)

        elif cmd == "9":
            game_info()

        elif cmd == "10":
            clear()
            laptop = True
            while laptop:
                clear()
                print("LAPTOP")
                print("\nApps")
                print("[A] Web")
                print("[B] NRS")
                print("[C] Secret Jobs Menu")
                pick = input("> ").lower()
                if pick == "a":
                    clear()
                    print("WEBSITES")
                    print("FBI.work")
                    print("System.exe")
                    search = input("> ")
                    if search.lower() == "fbi.work":
                        clear()
                        print("FBI is hiring want to apply? y/n")
                        ans = input("> ")
                        if ans.lower() == "y":
                            clear()
                            print("YOU ARE NOW FBI AGENT!")
                            job_type = "fbi"
                            has_job = "yes"
                            org = "fbi"
                            fight = "yes"
                            time.sleep(2)
                            laptop = False
                        else:
                            laptop = False
                    elif search.lower() == "money":
                    	clear()
                    	if web == "local":
                    		print("you need a better web system \nbuy one in the shop")
                    		time.sleep(1)
                    	else:
                    		print("MONEY!")
                    		print("don't use this web\nEVERY again")
                    		money += 400
                    		cheat += 6
                    		time.sleep(2)
                    		
                    elif search.lower() == "system.exe":
                        clear()
                        print("=== HACKER TERMINAL ===")
                        print(f"Hacks done: {hacks_done}/3 needed for HACKER JOB")
                        print("\nType 'hack' to hack ATM")
                        hack_cmd = input("> ").lower()
                        if hack_cmd == "hack":
                            if energy <= 10:
                                print("Too tired!")
                                time.sleep(1)
                            else:
                                success = random.randint(1, 2)
                                if success == 1:
                                    cash = random.randint(30, 80)
                                    print(f"HACK SUCCESS! +${cash}")
                                    money += cash
                                    hacks_done += 1
                                    energy -= 10
                                    if hacks_done >= 3:
                                        print("\n--- SECRET JOB UNLOCKED: HACKER ---")
                                        job_type = "hacker"
                                        has_job = "yes"
                                    time.sleep(2)
                                else:
                                    print("HACK FAILED! Police traced you!")
                                    wanted += 1
                                    time.sleep(1)
                        else:
                            clear()
                            print("Unknown command")
                            time.sleep(2)
                            laptop = False
                elif pick == "b":
                    clear()
                    headline = ["A car crash!","A theft is caught stealing ARRESTED!","A guy is arrested for ASSAULT"]
                    news = random.choice(headline)
                    print("NRS - National Radio station")
                    print(f"NEWS:\n{news}")
                    time.sleep(1)
                elif pick == "c":
                    clear()
                    print(f"=== SECRET JOBS ===")
                    print(f"Current: {job_type}")
                    print(f"Hacks: {hacks_done}/3")
                    print(f"Escapes: {escapes_done}/3 for DRIVER")
                    input("press enter...")
                    laptop = False
                else:
                    clear()
                    print("Unknown app!")
                    time.sleep(1)
                    laptop = False

        else:
            if cmd not in ["1","2","3","4","5","6","7","8","9","10"]:
                if status!= "police trace":
                    clear()
                    print("Unknown command")
                    print("\nor your organization doesn't let you\n")
                    input("press enter to continue: ")

    else:
        clear()
        where_police = random.choice(areas)
        print(f"Location:{location} \npolice location:{where_police}")
        print("\nActions")
        print("[1]Change location")
        print("[2]escape(escape the FBI 1 time)")
        esc = input("> ")
        if esc == "1":
            clear()
            print("Pick a location")
            print("[A] downtown")
            print("[B] market")
            print("[C] mall")
            print("[D] park")
            askA = input("> ")
            where_police = random.choice(areas)
            if askA == "A":
                clear()
                location = "downtown"
                if where_police == location:
                    print("THE POLICE IS THERE")
                    print("ARRESTED")
                    del_save()
                    break
                else:
                    print("Safe the police ain't there")
                    esc_c += 1
                    time.sleep(1)
            elif askA == "B":
                clear()
                location = "market"
                if where_police == location:
                    print("THE POLICE IS THERE")
                    print("ARRESTED")
                    del_save()
                    break
                else:
                    print("Safe the police ain't there")
                    esc_c += 1
                    time.sleep(1)
            elif askA == "C":
                clear()
                location = "mall"
                if where_police == location:
                    print("THE POLICE IS THERE")
                    print("ARRESTED")
                    del_save()
                    break
                else:
                    print("Safe the police ain't there")
                    esc_c += 1
                    time.sleep(1)
            elif askA == "D":
                clear()
                location = "park"
                if where_police == location:
                    print("THE POLICE IS THERE")
                    print("ARRESTED")
                    del_save()
                    break
                else:
                    print("Safe the police ain't there")
                    esc_c += 1
                    time.sleep(1)
            else:
                clear()
                print("Unknown location")
                time.sleep(2)
        elif esc == "2":
            clear()
            if esc_c >= 1:
                print("MISSON PASSED")
                print("\nYou successfully Escaped FBI\nwatch out reach wanted level 3\nyour done for")
                input("enter to continue:")
            else:
                print("escape the police 1 time FIRST")
                time.sleep(1)
        else:
            clear()
            print("unknown command")
            input("enter to continue: ")