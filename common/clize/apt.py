def install(target, *,  yes: 'y'=False):
    yes_flag = ""
    if yes:
        yes_flag = "-y"
    print("apt get install %s %s" % (target, yes_flag))

def search(target):
    print("apt search %s" % target)

if __name__ == "__main__":
    import clize
    clize.run(install, search)