import Calculator
import BookStore
import SLLStack

def menu_calculator() :
    calculator =  Calculator.Calculator()
    option=""
    while option != '0':
        print ("""
        1 Check mathematical expression 
        0 Return to main menu
        """)
        option=input()
        if option=="1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression) :
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")

        ''' 
        Add the menu options when needed
        '''

def menu_bookstore_system() :
    bookStore = BookStore.BookStore()
    option=""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Get cart best-seller
        7 Add a book by key to shopping cart
        8 Add a book by title prefix to shopping cart
        9 Search best-sellers with infix
        10 Sort the catalog
        11 Search book by prefix
        12 Display the first n books of catalog
        0 Return to main menu
        """)
        option=input() 
        if option=="r":
            bookStore.setRandomShoppingCart()
        elif option=="s":
            bookStore.setShoppingCart()
        elif option=="1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name) 
           # bookStore.pathLength(0, 159811)
        elif option=="2":
            i = int(("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option=="3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option=="4":
            bookStore.removeFromShoppingCart()
        elif option=="5":
            infix = input("Introduce the query to search: ")
            bookStore.searchBookByInfix(infix)
        elif option=="6":
            bookStore.getCartBestSeller()
        elif option=="7":
            key = input("Introduce the key to add to the shopping cart: ")
            bookStore.addBookByKey(key)
        elif option=="8":
            prefix = input("Intoduce the prefix to add to the shopping cart:")
            bookStore.addBookByPrefix(prefix)
        elif option== "9":
            in_fix = input("Enter infix: ")
            structure = int(input("Enter structure (1 or 2): "))
            titles = int(input("Enter max number of titles: "))
            bookStore.bestsellers_with(in_fix, structure, titles)
        elif option== "10":
            userInput = None
            while(userInput != 1 and userInput != 2 and userInput != 3):
                userInput = int(input("Choose an algorithm: \n\t1 - Merge Sort\n\t2 - Quick Sort (first element pivot)\n\t3 - Quick Sort (random element pivot)\nYour selection: "))
                if type(userInput) != int and userInput != 1 and userInput != 2 and userInput != 3:
                    print("Invalid algorithm")
            bookStore.sort_catalog(userInput)
        elif option== "11":
            pref = input("Enter prefix: ")
            v = None
            while(v != 1 and v != 2):
                v = int(input("Choose an algorithm:\n\t1 - Linear Search\n\t2 - Binary Search\n Your selection: "))
                if(v != 1 and v != 2):
                    print("Invalid algorithm")
            bookStore.search_by_prefix(pref, v)
        elif option== "12":
            display = int(input("Enter the number of books to display: "))
            bookStore.display_catalog(display)
        ''' 
        Add the menu options when needed
        '''

#main: Create the main menu
def main() :
    option=""
    while option != '0':
        print ("""
        1 Calculator
        2 Bookstore System
        3 Palindrome Test
        0 Exit/Quit
        """)
        option=input() 
        
        if option=="1":
            menu_calculator()
        elif option=="2":
            menu_bookstore_system()  
        elif option=="3":
            word = input("Enter a word/phrase: ")
            wordList = BookStore.DLList.DLList()
            for i in word:
                wordList.append(i)
            w = wordList.isPalindrome()
            if(w == True): 
                print("Result: Palindrome")
            else:
                print("Result: Not a Palindrome")

    # stack = SLLStack()
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)

if __name__ == "__main__":
  main()
