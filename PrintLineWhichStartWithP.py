# Print All The Line Starting With The Specific Letter
with open("example.txt","r") as fi:
    id = []
    inp = input("Enter The Letter: ")
    for i in (fi):
        if i.startswith(inp):
            print(i)
        else:
            print("Mf Its Not Here FUckOFF Now Lmao")
