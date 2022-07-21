import java.util.*;

public class Library {

	// Variables
	ArrayList<Books> library;														// Books stored in this ArrayList
	
	// Default constructor
	public Library() {
		this.library = new ArrayList<Books>();								// Dedicate storage depending on size of library
	}
	
	// Constructor if library size is given
	public Library(int librarySize) {	
		this.library = new ArrayList<Books>(librarySize);
	}
	
	// Methods
	
	// Add a book to the library
	public void addBook(Books book) {
		library.add(book);
	}
	
	// Remove a book from the library if it exists
	public void removeBook(Books book) {
		if (library.contains(book)) {
			library.remove(book);
		}
		else {
			System.out.println("That book doesn't exist in this library.");
		}
	}
	
	// Show the contents of library
	public void showLibrary() {	
		if (library.isEmpty()) {
			System.out.println("\tThere are no books in this library.");
		}
		else {
			for (int i = 0; i < library.size(); i++) {											// While the library we're viewing still has a book
				Books tempBook = library.get(i);											// Take first book			
				String tempTitle = tempBook.getTitle();
				String tempAuthor = tempBook.getAuthor();
				System.out.println("\t"+ tempTitle + ", By " + tempAuthor);	// Show book's bare-bone info
			}
		}
		System.out.println();																			// Prints nothing. Just wanted empty line to separate libraries
	}
	
	public static void main( String [ ] args ) {
	
		// Play around with the lines here to create as many books or libraries as needed
		// Create three libraries
		Library libraryOne = new Library(10);
		Library libraryTwo = new Library(7);
		Library libraryThree = new Library();
		
		// Make some books 
		Books firstBook = new Books("The Kite Runner", "Khaled Hosseini", "29-05-03", "Historical Fiction", false);
		Books secondBook = new Books("The Very Hungry Catterpillar", "Eric Carle", "03-06-69", "Children's", false);
		Books thirdBook = new Books("The Help", "Katheryn Stockett", "10-02-09", "Novel", true);
		// Books fourthBook = new Books(..
		// Books fifthBook = new Books(..
		
		
		// Try modifying
		libraryOne.addBook(firstBook);
		libraryOne.addBook(thirdBook);
		
		libraryTwo.addBook(secondBook);
		libraryTwo.removeBook(secondBook);
		
		libraryThree.addBook(firstBook);
		libraryThree.addBook(secondBook);
		libraryThree.addBook(thirdBook);
		
		// Results are..
		System.out.println("Library One:");
		libraryOne.showLibrary();
		System.out.println("Library Two:");
		libraryTwo.showLibrary();
		System.out.println("Library Three:");
		libraryThree.showLibrary();
	}
	
}
