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


