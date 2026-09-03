import React from "react";
import "../css/searchBar.css";
import { TextField } from "@mui/material";

export default function SearchBar({ value, onChange }:
    { value: string, onChange: (event: React.ChangeEvent<HTMLInputElement>) => void }
) {
    return (
        <TextField
            variant="filled"
            type="text"
            value={value}
            onChange={onChange}
            sx={{ width: 0.3 }}
            slotProps={{ input: { sx: { fontSize: 22 } } }}
            placeholder="Search a movie"
            size="small"
        />
    );
}