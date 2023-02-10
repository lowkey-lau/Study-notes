
import cards_tools

while True:
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是 【%s】" % action_str)

    if action_str in ["1", "2", "3"]:
        print('程序开始')

        if action_str == "1":
            print("执行 1 的函数")
            cards_tools.new_card()

        elif action_str == "2":
            print("执行 2 的函数")
            cards_tools.show_all()
            
        elif action_str == "3":
            print("执行 3 的函数")
            cards_tools.search_card()

    elif action_str == "0":
        print("欢迎再次使用文件系统")
        break
    else:
        print('你输入的不正确，请重新输入')


# print("*" * 50, '\n');
# print(
#     "欢迎使用【名片管理系统】V1.0\n\n"
#     "1.新建名片\n"
#     "2.显示全部\n"
#     "3.查询名片\n\n"
#     "0.退出系统\n"
#     )1

# print("*" * 50)