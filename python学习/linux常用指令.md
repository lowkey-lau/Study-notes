# 终端指令

## ls - list - 查看当前文件夹下的内容

## pwd - print wrok directory 查看当前所在文件夹

## cd[目录名] - change directory 切换文件夹

## touch[文件名] - touch 如果文件不存在，新建文件

## mkdir[目录名] - make directory 新建文件夹

## rm[文件名] - remove 删除文件或文件夹

## clear - clear 清屏

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
