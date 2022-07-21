import string
import Book
import ArrayList
import ArrayQueue
import RandomQueue
import MaxQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree 
import BinaryHeap 
import AdjacencyList 
import time
import algorithms



class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
    def __init__(self) :
        self.bookCatalog = ArrayList.ArrayList()
        self.shoppingCart = MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()
        

    def loadCatalog(self, fileName : str) :
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = DLList.DLList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()

            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                self.bookIndices.add(key, self.bookCatalog.size()-1)
                self.sortedTitleIndices.add(title, self.bookCatalog.size()-1)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

        
    def setRandomShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")
    
    def setShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")


    def removeFromCatalog(self, i : int) :
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i : int) :
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

   
    def searchBookByInfix(self, infix : str) :
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        # todo
        # --
        count = 0
        if(infix == ""):
            for x in range(0,50):
                try:
                    print(self.bookCatalog[x])
                except IndexError:
                    break
        else:
            for i in self.bookCatalog:
                if infix in i.title:
                    if count <= 49:
                        print(i)
                        count = 1 + count                   
        
        # --
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self) :
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        start_time = time.time()
        book = self.shoppingCart.max()
        print(book.title)
        elapsed_time = time.time() - start_time
        print(f"getCartBestSeller Completed in {elapsed_time} seconds")

    def addBookByKey(self, key):
        start_time = time.time()
        var = self.bookIndices.find(key)
        if(var != None):
            # get index
            # get the book for adding shopping cart
            # put the book inside shopping cart
            # print the title
            s = self.bookCatalog.get(var)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")
        #if not inside print did not find
        else:
            print("Book not found.")

    def addBookByPrefix(self, prefix):
        start_time = time.time()
        if prefix == "":
            elapsed_time = time.time() - start_time
            print(f"Book Not found \n{elapsed_time} seconds")
            return False
        else:
            index = self.sortedTitleIndices.find(prefix).v
            if index == None:
                elapsed_time = time.time() - start_time
                print(f"Book Not found \n{elapsed_time} seconds")
                return False
            else:
                s = self.bookCatalog.get(index)
                self.shoppingCart.add(s)
                elapsed_time = time.time() - start_time
                print(f"Added to shopping cart {s} \n{elapsed_time} seconds")
                return True

    def bestsellers_with(self, infix:string, structure:int, n=0):
        bestsellers = None
        if structure == 1:
            bestsellers = BinarySearchTree.BinarySearchTree()
        elif structure == 2:
            bestsellers = BinaryHeap.BinaryHeap()
        else:
            print("Invalid Data Structure.") 

        if n < 0:
            print("Invalid number of titles.") 
        elif bestsellers is not None:
            if infix == "":
                print("Invalid infix.") #infix can't be blank
            else:
                start_time = time.time()
                matches = 0
                for book in self.bookCatalog:
                    if infix in book.title:
                        if structure == 1:
                            bestsellers.add(book.rank, book)
                        else:
                            book.rank = -1 *book.rank
                            bestsellers.add(book)
                    

                if structure == 1:
                    books = reversed(bestsellers.in_order())
                    for book in books:
                        print(book.v)
                        matches += 1
                        if n != 0:
                            if matches == n:
                                break
                else:
                    while bestsellers.size() > 0:
                        book = bestsellers.remove()
                        book.rank = -1 * book.rank
                        print(book)

                        matches += 1
                        if n != 0:
                            if matches == n:
                                break
                elapsed_time = time.time() - start_time
                print(f"Displayed bestsellers_with({infix}, {structure}, {n}) in {elapsed_time} seconds.")

    def sort_catalog(self, s: int):
        if s==1:
            start_time = time.time()
            algorithms.merge_sort(self.bookCatalog)
            elapsed_time = time.time() - start_time
            print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds")
        elif s==2:
            start_time = time.time()
            algorithms.quick_sort(self.bookCatalog, False)
            elapsed_time = time.time() - start_time
            print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds")
        elif s==3:
            start_time = time.time()
            algorithms.quick_sort(self.bookCatalog, True)
            elapsed_time = time.time() - start_time
            print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def search_by_prefix(self, prefix, algo):
        bookcatalog2 = ArrayList.ArrayList()
        for x in self.bookCatalog:
            bookcatalog2.append(x)
        foundbooks = 0
        start_time = time.time()
        if(algo == 1):
            i = 0
            while i < 1:
                index = None
                b = Book.Book("1", prefix, "1", "1", "1")
                index = algorithms.linear_search(bookcatalog2, b)
                if(index >= 0):
                    foundbooks += 1
                    print(bookcatalog2.remove(index))
                    i -= 1
                i += 1
        elif(algo == 2):
            algorithms.merge_sort(bookcatalog2)
            i = 0
            while i < 1:
                index = None
                b = Book.Book("1", prefix, "1", "1", "1")
                index = algorithms.binary_search(bookcatalog2, b)
                if(index >= 0):
                    foundbooks += 1
                    print(bookcatalog2.remove(index))
                    i -= 1
                i += 1
        elapsed_time = time.time() - start_time
        print(f"Found {foundbooks} books with prefix {prefix} in {elapsed_time} seconds.")


    def display_catalog(self, n):
        for i in range(0, n):
            print(self.bookCatalog.get(i))