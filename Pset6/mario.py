def mario():
    try:
        height = int(input("Height: "))
    except ValueError:
        mario()
    else:
        if 8 >= height > 0:
            spaces = [" " for i in range(height - 1)]
            hash = "#"
            for i in range(height):
                str = ""
                print(f"{str.join(spaces)}{hash}  {hash}{str.join(spaces)}")
                if len(spaces) > 0:
                    spaces.pop(-1)
                hash += "#"
        else:
            mario()


mario()
