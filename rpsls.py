#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ���֥ѩ
���ڣ�2020.4.10
"""
import random
def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="��":
        return 2
    elif name=="����":
        return 3
    elif name=="����":
        return 4
    else:
       print("Error: No Correct Name.")# ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
       
def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        return "ʯͷ"
    elif number==1:
        return "ʷ����"
    elif number==2:
        return "��"
    elif number==3:
        return "����"
    elif number==4:
        return "����"
    else:
        print("Error: No Correct Name.")# ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
        
def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    print("---------------------")# ���"-------- "���зָ�
    print("����ѡ��Ϊ:",player_choice)# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
    player_number=name_to_number(player_choice) # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    comp_number=random.randrange(0,4)# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    comp_choice=number_to_name(comp_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    print("�������ѡ��Ϊ:",comp_choice)# ����Ļ����ʾ�����ѡ����������
    if player_number==0 and (comp_number==3 or comp_number==4):
         print("��Ӯ��!")
    elif player_number==1 and (comp_number==0 or comp_number==4):
         print("��Ӯ��!")
    elif player_number==2 and (comp_number==0 or comp_number==1):
         print("��Ӯ��!")
    elif player_number==3 and (comp_number==2 or comp_number==1):
         print("��Ӯ��!")
    elif player_number==4 and (comp_number==2 or comp_number==3):
         print("��Ӯ��!")
    elif player_number==comp_number:
         print("���ͼ������ѡ��һ��.")
    else:
          print("����Ӯ��!")# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
           
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
    
    
