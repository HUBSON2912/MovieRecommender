import { createContext, useEffect, useState } from "react";
import Header from "./components/header";
import "./css/App.css";
import type { Page, PageContextType } from "./types";
import SearchBar from "./components/searchBar";


export const CurrentPageContext = createContext<PageContextType>({ page: "search", setPage: () => { } });

function App() {
    const [currentPage, setCurrentPage] = useState<Page>("search");

    const [searchTextInput, setSearchTextInput] = useState<string>("");
    const handleWriting = (event: React.ChangeEvent<HTMLInputElement>) => {
        setSearchTextInput(event.currentTarget.value);
    }

    useEffect(() => {
        // < 2 to catch movies like IT or E.T.
        if (searchTextInput.length < 2)
            return;

        // TODO send AJAX request to the api for movies

    }, [searchTextInput])

    return (
        <CurrentPageContext value={{ page: currentPage, setPage: setCurrentPage }}>
            <Header />
            <main>
                <SearchBar value={searchTextInput} onChange={handleWriting} />
            </main>
        </CurrentPageContext>
    )
}

export default App;
