import React from "react";
import "../css/searchBar.css";
import { Box, Button, TextField } from "@mui/material";

function isAlphanumeric(input:string):boolean {
    return Boolean(input.match(/^[0-9a-zA-Z ]*$/gm))
}

export default function SearchBar({ value, onChange, onSearch, onClear}:
    {
        value: string,
        onChange: React.ChangeEventHandler<HTMLInputElement>,
        onSearch: () => void
        onClear: () => void
    }) {
    return (
        <>
            <TextField
                variant="filled"
                type="text"
                value={value}
                sx={{ width: 0.3, margin: 1 }}
                onChange={onChange}
                slotProps={{ input: { sx: { fontSize: 22 } } }}
                placeholder="Search a movie"
                size="small"
            />
            <Box>
                <Button
                    variant="outlined"
                    sx={{ margin: 1 }}
                    onClick={onSearch}
                    disabled={value=="" || !isAlphanumeric(value)}
                >Search</Button>
                <Button
                    variant="outlined"
                    sx={{ margin: 1 }}
                    onClick={onClear}
                >Clear</Button>
            </Box>
        </>
    );
}