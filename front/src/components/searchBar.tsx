import React from "react";
import "../css/searchBar.css";
import { Button, TextField } from "@mui/material";

export default function SearchBar({ value, onChange, onSearch }:
    {
        value: string,
        onChange: React.ChangeEventHandler<HTMLInputElement>,
        onSearch: ()=>void
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
            <Button
                variant="outlined"
                sx={{ margin: 1 }}
                onClick={onSearch}
            >Search</Button>
        </>
    );
}