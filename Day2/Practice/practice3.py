bike = str(input("Enter the bike name: "))

match bike:
    case "Yamha":
        print("Bike is Yamha")
    case "Honda":
        print("Bike is Honda")
    case "Suzuki":
        print("Bike is Suzuki")
    case _ :
        print("It must be a superbike")
