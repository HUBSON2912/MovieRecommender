import React from "react";
import "../css/searchBar.css";
import { TextField } from "@mui/material";

export default function SearchBar({ value, onChange }:
    { value: string, onChange: (event:React.ChangeEvent<HTMLInputElement>) => void }
) {
    return (
        <TextField variant="filled" type="text" value={value} onChange={onChange} />
        // <input className="bar" name="searchBar" value={value} onChange={onChange}></input>
    );
}