# 集成dex2jar和JD-GUI实现命令行快速反编译查看apk文件
**注意，仅限于类Unix系统（mac，Linux...），需要Python环境支持！**

## HOW TO USE
### 1.下载工程解压并复制到本地任意目录
### 2.添加本地工程地址到系统环境变量
#### 2.1 打开终端，输入 open -e .bash_profile
#### 2.2 添加本地工程路径至bash_profile文件并保存。例如：
	# dexlooker
	export PATH=$PATH:/Users/wangxiandeng/Documents/MyCoding/PythonWork/DexLooker/dexlooker
### 3.现在就可以使用了：在终端输入 dexlooker.py，拖入你的apk文件，将会自动为你反编译apk并打开JD-GUI查看jar文件

**（喜欢的话给个star哦）**
         