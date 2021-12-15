clize
-----------

用于将python函数包装成命令行工具。
自动根据函数的参数名、默认值、注释来生成flag和help，十分简单方便。

URL: https://github.com/epsy/clize

简单用法:

    # hello.py
    from clize import run

    def hello_world(name=None, *, no_capitalize=False):
        """Greets the world or the given name.

        :param name: If specified, only greet this person.
        :param no_capitalize: Don't capitalize the given name.
        """
        if name:
            if not no_capitalize:
                name = name.title()
            return 'Hello {0}!'.format(name)
        return 'Hello world!'

    if __name__ == '__main__':
        run(hello_world)


简单的run一下一个函数，就可以把它包装成一个命令行工具：

前述样例执行`python3 hello.py --help` 即会生成很详细的帮助信息：

    Usage: hello.py [OPTIONS] name

    Greets the world or the given name.

    Positional arguments:
      name   If specified, only greet this person.

    Options:
      --no-capitalize   Don't capitalize the given name.

    Other actions:
      -h, --help   Show the help

sub command的支持也很天然：

    # apt.py
    def install(target, yes: 'y'=False):
        yes_flag = ""
        if yes:
            yes_flag = "-y"
        print("apt get install %s %s" % (target, yes_flag))

    def search(target):
        print("apt search %s" % target)
    
    if __name__ == "__main__":
        import clize
        clize.run(install, search)

这样一个简单的样例就支持了install和search两个sub command，模仿了出了apt命令的sub command。

这项目要是能支持自动生成autocompelte就堪称完美了。

更多官方样例：