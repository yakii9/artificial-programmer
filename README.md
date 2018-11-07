# Artificial Programmer
接受形式化的需求，输出可执行程序。

## 路线图
经过两天来的文献研究和观看公开课，我有了一些清晰的思路，其实建立“人工编程者”（AP）最基本的一个必要条件就是建立一个能够晰地描述整个从“提出需求”到“生成可执行程序”的模型。  
所以，整个工作的第一步，是对编程过程进行建模。

## 目录结构
- config：存放一些基础设置json文件
- modules： 功能模块
    + base 一些基本工具类：
        * file_helper 关于文件操作的类
        * url_helper 关于网页处理的类
        * handle_timeout 一个控制函数超时的装饰器
    + parse 一些内容解析器（包含文字语义解析等）
    + save  将内容（网址、数据资源）保存的类
- main.js 程序的主入口
