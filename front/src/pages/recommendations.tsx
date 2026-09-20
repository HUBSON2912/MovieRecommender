import { useEffect, useState } from "react";
import { getModelsList, getRecommendations, retrainNewModel } from "../api/models";
import SelectList from "../components/selectList";
import { Box, Button, type SxProps } from "@mui/material";
import type { Theme } from "@mui/material/styles";
import type { Movie } from "../types";
import MovieCard from "../components/movieCard";
import MovieList from "../components/movieList";

export default function RecommendationsPage() {
    const [modelNames, setModelNames] = useState<string[]>([]);
    useEffect(() => {
        // load list of trained models
        getModelsList().then(res => setModelNames(res.sort())).catch();
    }, []);

    const [selectedModel, setSelectedModel] = useState<string | null>(null);


    const [recommendedMovies, setRecommendedMovies] = useState<Movie[]>([])
    const handleGetRecommendations = () => {
        if (!selectedModel)
            return;

        getRecommendations(selectedModel)
            .then(res => setRecommendedMovies(res))
            .catch(err => console.error(err));
    }

    // todo if no rated movies -> "You must to rate movies"
    return (
        <>
            <Box sx={styles.selectModelContainer}>
                <SelectList items={modelNames} onClickItem={setSelectedModel} selected={selectedModel} title="Select model" />
                <Box sx={styles.buttonPanel}>
                    <Button
                        variant="outlined"
                        disabled={selectedModel == null}
                        onClick={handleGetRecommendations}
                    >Run</Button>

                    <Button variant="outlined" onClick={() => retrainNewModel()}>Retrain new</Button>
                </Box>
            </Box>
            
            <MovieList movies={recommendedMovies}/>
        </>
    );
}

const styles: Record<string, SxProps<Theme>> = {
    selectModelContainer: {
        display: "flex",
        alignContent: "center",
        alignItems: "center",
        gap: 5
    },
    buttonPanel: {
        display: "flex",
        flexDirection: "column",
        gap: 2
    }
}