
public class Books extends Library{

	// Variables
	String title;
	String author;
	String publishDate;							// Publishing date of book, DDMMYY
	String genre;										// Horror, Drama, Sci-fi, etc
	boolean borrowed;
	
	// Default constructor if no parameters specified, never used, but here just for convention
	public Books() {								
	}
	
	// Constructor if parameters are specified
	public Books(String title, String  author, String publishDate, String genre, boolean borrowed) {								
		this.title = title;
		this.author = author;	
		this.publishDate = publishDate;
		this.genre = genre;
		this.borrowed = borrowed;
	}
	
	// Getters
	public String getTitle() {
		return title;
	}
	public String getAuthor() {
		return author;
	}
	
	public String getPublishDate() {
		return publishDate;
	}
	
	public String getGenre() {
		return genre;
	}
	
	public boolean getAvailable() {
		return borrowed;
	}
	
	// Setters
	public void setTitle(String title) {
		this.title = title;
	}
	public void setAuthor(String author) {
		this.author = author;
	}
	
	public void setPublishDate(String publishDate) {
		this.publishDate = publishDate;
	}
	
	public void setGenre(String genre) {
		this.genre = genre;
	}
	
	public void setAvailable(boolean borrowed) {
		this.borrowed = borrowed;
	}
	
}
