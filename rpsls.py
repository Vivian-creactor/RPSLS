#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：胡芝雪
日期：2020.4.10
"""
import random
def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":
        return 0
    elif name=="史波克":
        return 1
    elif name=="布":
        return 2
    elif name=="蜥蜴":
        return 3
    elif name=="剪刀":
        return 4
    else:
       print("Error: No Correct Name.")# 使用if/elif/else语句将各游戏对象对应到不同的整数
       
def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        return "石头"
    elif number==1:
        return "史波克"
    elif number==2:
        return "布"
    elif number==3:
        return "蜥蜴"
    elif number==4:
        return "剪刀"
    else:
        print("Error: No Correct Name.")# 使用if/elif/else语句将不同的整数对应到游戏的不同对象
        
def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    print("---------------------")# 输出"-------- "进行分割
    print("您的选择为:",player_choice)# 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
    player_number=name_to_number(player_choice) # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
    comp_number=random.randrange(0,4)# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
    comp_choice=number_to_name(comp_number)# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
    print("计算机的选择为:",comp_choice)# 在屏幕上显示计算机选择的随机对象
    if player_number==0 and (comp_number==3 or comp_number==4):
         print("您赢了!")
    elif player_number==1 and (comp_number==0 or comp_number==4):
         print("您赢了!")
    elif player_number==2 and (comp_number==0 or comp_number==1):
         print("您赢了!")
    elif player_number==3 and (comp_number==2 or comp_number==1):
         print("您赢了!")
    elif player_number==4 and (comp_number==2 or comp_number==3):
         print("您赢了!")
    elif player_number==comp_number:
         print("您和计算机的选择一样.")
    else:
          print("机器赢了!")# 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
           
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
    
    
