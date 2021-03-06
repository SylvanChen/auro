# ANTLR 框架学习笔记

### 学习目标
* 识别具有固定语法文本中的语法规则，构建语法体系
* 构建语法，从 Json 这样的简单语法开始到 R 语言这样的复杂语法，都能构建
* 基于语法分析树搭建应用程序
* 自定义领域特定错误识别模式
* 通过Java操作对语法进行控制

### 段落结构
1. 背景知识点 + ANTLR 能力介绍
2. 使用树形遍历来设计语法，以及构建应用程序
3. 自定义 ALTLR 语法解析错误处理器
4. ALTLR 的使用规则和运行库

### 使用语法规则来检测分析文本
1. 定义一套语法规则
2. 解析文本
3. 定义一套访问操作
4. 遍历树形结构并执行访问操作
