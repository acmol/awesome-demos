gcc main.c -o main -lm
gcc -Os -nostdlib -nodefaultlibs -fPIC -Wl,-shared hook.c -o libhook.so

libm_so=$(ldd main | grep libm.so | awk '{print $3}')
so_name=`basename $libm_so`
python3 hook.py "$libm_so" ./$so_name

echo 'normal run:'
LD_LIBRARY_PATH="" ./main 1
echo

echo 'run with hooked libm.so:'
LD_LIBRARY_PATH=. ./main 1

