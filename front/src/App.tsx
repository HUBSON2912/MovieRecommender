import { createContext, useState } from "react";
import Header from "./components/header";
import "./css/App.css";
import type { Page, PageContextType } from "./types";
import { Box } from "@mui/material";
import type { SxProps } from "@mui/material/styles";
import type { Theme } from "@mui/material/styles";
import SearchPage from "./pages/search";


export const CurrentPageContext = createContext<PageContextType>({ page: "search", setPage: () => { } });

function App() {
    const [currentPage, setCurrentPage] = useState<Page>("search");
    

    return (
        <CurrentPageContext value={{ page: currentPage, setPage: setCurrentPage }}>
            <Box sx={styles.container}>

                <Header />
                <main>
                    <SearchPage />
                </main>

            </Box>
        </CurrentPageContext>
    )
}

const styles: Record<string, SxProps<Theme>> = {
    container: {
        color: "text.primary",
        backgroundColor: "background.default",
        // height: "100vh",
        minHeight: "100vh",
        fontSize: 22,
        width: 1
    },
};

export default App;
