import React from "react";
import "../css/searchBar.css";

export default function SearchBar({ value, onChange }:
    { value: string, onChange: (event:React.ChangeEvent<HTMLInputElement>) => void }
) {
    return (
        <input className="bar" name="searchBar" value={value} onChange={onChange}></input>
    );
}