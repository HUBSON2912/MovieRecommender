import { useEffect, useState } from "react";
import { getModelsList } from "../api/models";
import SelectList from "../components/selectList";
import { Box, Button, type SxProps } from "@mui/material";
import type { Theme } from "@mui/material/styles";

export default function RecommendationsPage() {
    const [modelNames, setModelNames] = useState<string[]>([]);
    useEffect(() => {
        // load list of trained models
        getModelsList().then(res => setModelNames(res.sort())).catch();
    }, []);

    const [selectedModel, setSelectedModel] = useState<string | null>(null);

    // todo if no rated movies -> "You must to rate movies"
    return (
        <Box sx={styles.selectModelContainer}>
            <SelectList items={modelNames} onClickItem={setSelectedModel} selected={selectedModel} title="Select model" />
            <Box sx={styles.buttonPanel}>
                <Button variant="outlined" disabled={selectedModel==null}>Run</Button>
                <Button variant="outlined">Retrain new</Button>
            </Box>
        </Box>
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