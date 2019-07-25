import time
import random

def displayInformation(name, health, attack):
    if name == 'player':
        print('【玩家】\n'+'血量：'+str(health)+'\n攻击：'+str(attack))
        print('------------------------')
    elif name == 'enemy':
        print('【敌人】\n'+'血量：'+str(health)+'\n攻击：'+str(attack))
        print('------------------------')
    time.sleep(1.5)


player_win_count = 0
enemy_win_count = 0


for i in range(1, 4):
    print('Round:', i)
    playerHealth = random.randint(100, 150)
    enemyHealth = random.randint(100, 150)

    playerAttack = random.randint(30, 50)
    enemyAttack = random.randint(30, 50)
    displayInformation('player', playerHealth, playerAttack)
    displayInformation('enemy', enemyHealth, enemyAttack)

    while playerHealth > 0 and enemyHealth > 0:
        enemyHealth -= playerAttack
        print('你发起了攻击，【敌人】剩余血量', enemyHealth)
        playerHealth -= enemyAttack
        print('敌人向你发起了攻击，【玩家】剩余血量', playerHealth)
        print('------------------------') 
        time.sleep(1.5)

    if playerHealth < 0 and enemyHealth < 0:
        print('Round: ', i, '平手')
        pass
    elif playerHealth > 0:
        player_win_count += 1
        print('Round:', i, '玩家赢')
    else:
        enemy_win_count += 1
        print('Round:', i, '敌人赢')

if player_win_count == 2:
    print('【玩家】胜利')
elif enemy_win_count == 2:
    print('【玩家】失败')
else:
    print('平手')