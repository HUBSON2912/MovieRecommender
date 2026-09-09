import { useEffect, useState } from "react";
import { getModelsList } from "../api/models";

export default function RecommendationsPage() {
    const [modelNames, setModelNames]=useState<string[]>([]);
    useEffect(()=>{
        getModelsList().then(setModelNames).catch();
    },[]);
    return (<p>{JSON.stringify(modelNames)}</p>);
}