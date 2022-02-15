lief
--------------

一款跨平台的二进制可执行文件信息读取、修改工具。

如果你有一个二进制，希望替换掉其中的一些函数，可以尝试一下lief。
（当然，如果LD_PRELOAD可以解决问题，你可以先考虑用LD_PRELOAD）

安装: `pip3 install lief`

demo：

    bash demo.sh

修改libm.so，将其中的exp函数替换为libhook.so中的hook函数：

    import sys
    import lief

    libm_so_path = sys.argv[1]
    libm_so_output_path = sys.argv[2]

    libhook = lief.parse('./libhook.so')
    libm = lief.parse(libm_so_path)

    exp = libm.get_symbol('exp')
    hook = libhook.get_symbol('hook')

    seg = libm.add(libhook.segments[0])

    exp.value = seg.virtual_address + hook.value
    libm.write(libm_so_output_path)






