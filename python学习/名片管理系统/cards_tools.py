card_list = []


def show_menu():
    print("*" * 50)
    print("")
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("")
    print("*" * 50)


def new_card():
    """新增名片"""

    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    card_dict = {
            "name": name_str, 
            "phone": phone_str, 
            "qq": qq_str, 
            "email": email_str
        }
    card_list.append(card_dict)

    print(card_list)

    print("添加 %s 的名片成功！" % name_str)



def show_all():
    """显示名片列表"""

    if len(card_list) == 0:
        print("当前没有记录，请前往创建")
        return

    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t\t\t")
    
    print("")
    print("=" * 50)

    for card_dict in card_list:
        print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))



def search_card():
    """查询用户信息"""

    name_str = input("请输入需要查询的用户名称：")

    for card_dict in card_list:
        if card_dict["name"] == name_str:
            print("姓名\t\t\t\t电话\t\t\t\tQQ\t\t\t\t邮箱")
            print("=" * 50)
            print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))
            
            deal_card(card_dict)

            break
        
        else:
            print("抱歉没找到用户 %s" % name_str)



def deal_card(find_dict):
    action_str = input("请输入对名片的操作："
                        "[1] 修改 [2]删除 [0]返回上级菜单")

    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "请输入名称[回车不修改]")
        find_dict["phone"] = input_card_info(find_dict["phone"], "请输入电话[回车不修改]")
        find_dict["qq"] = input_card_info(find_dict["qq"], "请输入QQ[回车不修改]")
        find_dict["email"] = input_card_info(find_dict["email"], "请输入邮箱[回车不修改]")

        print("修改名片成功")

    elif action_str == "2":

        card_list.remove(find_dict)

        print("删除名片成功！")


def input_card_info(dict_val, tips_val):
    

    input_val = input(tips_val)

    if len(input_val) > 0:
        return input_val
    else:
        return dict_val
    
