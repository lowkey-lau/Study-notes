# 终端指令

## ls - list - 查看当前文件夹下的内容

## pwd - print wrok directory 查看当前所在文件夹

## cd[目录名] - change directory 切换文件夹

## touch[文件名] - touch 如果文件不存在，新建文件

## mkdir[目录名] - make directory 新建文件夹

## rm[文件名] - remove 删除文件或文件夹

## clear - clear 清屏

## tree - tree 显示目录树结构

---

<kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>=</kbd>：放大终端字体大小

<kbd>ctrl</kbd> + <kbd>-</kbd>：缩小终端字体大小

---

# 创建隐藏文件

创建文件前加 `.` 即可

```linux
touch .123.txt //创建隐藏文件
ls -a //查看所有文件（包括隐藏文件）
rm .123.txt //删除隐藏文件

ls -l -h 可以查看文件的大小，更直观

cd + ~ 快速回根目录

cd + .. 会到上一级目录

```

---

# 文件相关

## cp [复制文件路径] [目标文件路径] - copy 复制某个文件到指定目标

## mv [移动目录文件] [目标文件路径] - move 移动某个文件到指定目标

## cat - concatenate 查看文件内容，会一次性全部显示出来 (适合内容少时)

## more - more 查看文件内容，会出现终端屏幕的内容，剩余的百分比显示（内容多时建议使用）

## grep [搜索关键字] [搜索文件路径] - grep 搜索功能

`-n` :显示匹配行及行号
`-v`：搜索不包含关键字的内容
`-i`: 不区分大小写

`echo` 输出内容；

`>` 重定向 把终端输出的内容输出文件 echo ddd > a

`>>` 在文件输出/追加内容 echo aaa >> a

`|` 管道

## shutdown 关机 控制服务器的开关机

-r 重新启动
