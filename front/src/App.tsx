import { createContext, useState } from "react";
import Header from "./components/header";
import "./css/App.css";
import type { RatingsContextType, Page, PageContextType, Rate } from "./types";
import { Box } from "@mui/material";
import type { SxProps } from "@mui/material/styles";
import type { Theme } from "@mui/material/styles";
import SearchPage from "./pages/search";


export const CurrentPageContext = createContext<PageContextType>({ page: "search", setPage: () => { } });
export const RatingsContext = createContext<RatingsContextType>({ ratings: [], setRatings: () => { }, delRatings: () => { } })

function App() {
    const [currentPage, setCurrentPage] = useState<Page>("search");
    const [ratings, setRatings] = useState<Rate[]>([]);
    const handleSetRatings = (r: Rate) => {
        let editBuffer: Rate[] = ratings;

        for (let i = 0; i < editBuffer.length; i++) {
            if (editBuffer[i].movieId == r.movieId) {
                editBuffer[i].rate = r.rate;
                setRatings(editBuffer);
                return;
            }
        }
        editBuffer.push(r);
        setRatings(editBuffer);
    }
    const handleDelRatings = (mId: number) => {
        let editBuffer: Rate[] = ratings;
        for (let i = 0; i < editBuffer.length; i++) {
            if (editBuffer[i].movieId == mId) {
                editBuffer.splice(i, 1);  // delete one element
                return;
            }
        }
        console.info("Nothing deleted");
    }

    return (
        <CurrentPageContext value={{ page: currentPage, setPage: setCurrentPage }}>
            <RatingsContext value={{ ratings: ratings, setRatings: handleSetRatings, delRatings: handleDelRatings }}>
                <Box sx={styles.container}>
                    <Header />
                    <main>
                        <SearchPage />
                    </main>
                </Box>
            </RatingsContext>
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
