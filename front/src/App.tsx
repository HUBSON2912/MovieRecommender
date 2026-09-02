import { createContext, useState } from "react";
import Header from "./components/header";
import "./css/App.css";
import type { Page, PageContextType } from "./types";


export const CurrentPageContext = createContext<PageContextType>({ page: "search", setPage: () => { } });

function App() {
    const [currentPage, setCurrentPage] = useState<Page>("search");

    return (
        <CurrentPageContext value={{ page: currentPage, setPage: setCurrentPage }}>
            <Header />
        </CurrentPageContext>
    )
}

export default App;
