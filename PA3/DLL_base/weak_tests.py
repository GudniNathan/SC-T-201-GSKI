import sys
from dll import DLL


def main():

    orig_stdout = sys.stdout
    fout = open('out.txt', 'w+')
    sys.stdout = fout

    print("\n\nTESTING THE BASIC STUFF\n")

    dll = DLL()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("D")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("E")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("1")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("2")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("3")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("4")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("VALUE")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(8)
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(2)
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(-1)
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(18)
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(0)
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))

    print("\n\nTESTING MORE COMPLEX STUFF\n")

    dll = DLL()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B1")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B2")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.reverse()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B3")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))

    dll.remove_all("C")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.sort()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))

    dll.remove_all("A")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))

    dll.reverse()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))

    dll.remove_all("C")
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))

    dll.move_to_next()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " +
          str(dll.get_value()) + "   -   size: " + str(len(dll)))

    sys.stdout = orig_stdout
    fout.close()


if __name__ == "__main__":
    main()
