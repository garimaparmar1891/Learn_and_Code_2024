class Book {
    function getBookTitle() {
        return "A Great Book";
    }

    function getBookAuthor() {
        return "John Doe";
    }
}

class Reader implements Book{
    function turnBookPage() {
        // pointer to next page
    }

    function getBookCurrentPageContent() {
        return "current page content";
    }
}

class LibraryManager implements Book{
    function getBookLocation() {
        // returns the position in the library
        // ie. shelf number & room number
    }

    function saveBook(Book $book) {
        $filename = '/documents/'. $this->getBookTitle(). ' - ' . $this->getBookAuthor();
        filePutContents($filename, serialize($this));
    }
}

interface Printer {
    function printPage(string $pageContent);
}

class PlainTextPrinter implements Printer {
    function printPage(string $pageContent) {
        echo $pageContent;
    }
}

class HtmlPrinter implements Printer {
    function printPage(string $pageContent) {
        echo '<div style="single-page">' . $pageContent . '</div>';
    }
}
