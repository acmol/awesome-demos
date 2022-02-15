# awesome-demos
Learn awesome projects by simple demos

收集一些比较赞的项目，并通过简单的几个demo展示基本用法。

收集的demo特点：

1. 安装简单，或无需安装即可在线试用
2. 简单用懂
3. 项目实用


## 通用项目

### [clize](./common/clize/README.md) 

 用于将python函数包装成命令行工具。
自动根据函数的参数名、默认值、注释来生成flag和help，十分简单方便。 

### [jq](./common/jq/README.md) 

 命令行解析json利器。 



## 开发工具

### [openvscode-server](./dev/openvscode-server/README.md) 

 一个可以在自己服务器上搭建的云端IDE，下载解压后，一条命令即可启动一个可以在浏览器里打开的vscode开发环境。
gitpod不适合用在公司对数据安全性有要求、不允许使用外部服务的场景，这时，你可以使用openvscode-server。
它是gitpod所在公司出品的开源项目。 

### [gitpod](./dev/gitpod/README.md) 

 基于vscode的一个与github & gitlab深度集成的云IDE，用起来和本地vscode一模一样。

支持自定义开发环境docker镜像，可以 ctrl + j 打开terminal为所欲为。

开源项目无需配置直接免费使用50个小时，也支持企业自己服务器上搭建私有集群。 

### [github.dev](./dev/github.dev/README.md) 

 github官方云端代码编辑器。

看着和gitpod.io基本一样，但我没说它是IDE是因为它虽然也是基于vscode online，但没有提供编译、执行的云端容器，所以只能算个代码编辑器。
(以前似乎提供过开发环境，可能是太烧钱了，暂时找不到了) 



## 操作系统相关

### [lief](./os/lief/README.md) 

 一款跨平台的二进制可执行文件信息读取、修改工具。

如果你有一个二进制，希望替换掉其中的一些函数，可以尝试一下lief。
（当然，如果LD_PRELOAD可以解决问题，你可以先考虑用LD_PRELOAD） 

