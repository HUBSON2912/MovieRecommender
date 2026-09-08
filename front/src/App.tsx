import { createContext, useEffect, useState } from "react";
import Header from "./components/header";
import "./css/App.css";
import type { RatingsContextType, Page, PageContextType, Rate } from "./types";
import { Box } from "@mui/material";
import type { SxProps } from "@mui/material/styles";
import type { Theme } from "@mui/material/styles";
import SearchPage from "./pages/search";


export const CurrentPageContext = createContext<PageContextType>({ page: "search", setPage: () => { } });
export const RatingsContext = createContext<RatingsContextType>({ ratings: [], setRatings: () => { }, delRatings: () => { }, getRate: () => { } })

function App() {
    const [currentPage, setCurrentPage] = useState<Page>("search");
    const [ratings, setRatings] = useState<Rate[]>([]);
    const handleSetRatings = (r: Rate) => {
        let editBuffer: Rate[] = ratings;

        for (let i = 0; i < editBuffer.length; i++) {
            if (editBuffer[i].movieId == r.movieId) {
                editBuffer[i].rate = r.rate;
                setRatings([...editBuffer]);
                return;
            }
        }
        setRatings([...editBuffer, r]);
        localStorage.setItem("ratings", JSON.stringify([...editBuffer, r]));
    }
    const handleDelRatings = (mId: number) => {
        let editBuffer: Rate[] = ratings;
        for (let i = 0; i < editBuffer.length; i++) {
            if (editBuffer[i].movieId == mId) {
                editBuffer.splice(i, 1);  // delete one element
                setRatings([...editBuffer]);
                localStorage.setItem("ratings",JSON.stringify([...editBuffer]));
                return;
            }
        }
        console.info("Nothing deleted");
    }
    const handleGetRate = (mId: number): number | undefined => {
        const foundRate = ratings.find(r => r.movieId == mId);
        if (foundRate)
            return foundRate.rate;
        return undefined;
    }
    // load ratings from localstorage
    useEffect(() => {
        let savedRatings = localStorage.getItem("ratings");
        if (!savedRatings)
            savedRatings = JSON.stringify([]);

        setRatings(JSON.parse(savedRatings));
    }, []);

    return (
        <CurrentPageContext value={{ page: currentPage, setPage: setCurrentPage }}>
            <RatingsContext value={{ ratings: ratings, setRatings: handleSetRatings, delRatings: handleDelRatings, getRate: handleGetRate }}>
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
